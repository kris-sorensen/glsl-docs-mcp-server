from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
import re
from typing import Dict, List
import time

mcp = FastMCP("GLSL_Docs_MCP")

# Documentation sources
DOCS_SITES = {
    "book_of_shaders": {
        "base_url": "https://thebookofshaders.com",
        "name": "The Book of Shaders"
    },
    "opengl_org": {
        "base_url": "https://www.opengl.org",
        "name": "OpenGL.org"
    },
    "khronos_opengl": {
        "base_url": "https://www.khronos.org/opengl",
        "name": "Khronos OpenGL"
    },
    "maxime_heckel_shaders": {
        "url": "https://blog.maximeheckel.com/posts/the-study-of-shaders-with-react-three-fiber/",
        "name": "Maxime Heckel - R3F Shaders"
    },
    "shadertoy_to_r3f": {
        "url": "https://www.thefrontdev.co.uk/workflow-from-shadertoy-to-react-three-fiber-r3f/",
        "name": "TheFrontDev - Shadertoy to R3F"
    },
    "codrops_reveal": {
        "url": "https://tympanus.net/codrops/2024/12/02/how-to-code-a-shader-based-reveal-effect-with-react-three-fiber-glsl/",
        "name": "Codrops - Shader Reveal Effect"
    },
    "gpu_particles": {
        "url": "https://www.thefrontdev.co.uk/how-to-create-gpu-particles-in-react-three-fiber-(r3f)/",
        "name": "TheFrontDev - GPU Particles"
    },
    "maxime_particles": {
        "url": "https://blog.maximeheckel.com/posts/the-magical-world-of-particles-with-react-three-fiber-and-shaders/",
        "name": "Maxime Heckel - Advanced Particles"
    },
    "curve_particles": {
        "url": "https://www.thefrontdev.co.uk/creating-amazing-particle-effect-along-a-curve-in-react-three-fiber/",
        "name": "TheFrontDev - Curve Particles"
    },
    "threejs_manual_shadertoy": {
        "url": "https://threejs.org/manual/#en/shadertoy",
        "name": "Three.js Manual - Shadertoy"
    },
    "threejs_manual_shaders": {
        "url": "https://threejs.org/manual/#en/shaders",
        "name": "Three.js Manual - Shaders"
    },
    "webgl_fundamentals": {
        "url": "https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html",
        "name": "WebGL Fundamentals - Shaders"
    },
    "glsl_reference": {
        "base_url": "https://registry.khronos.org/OpenGL-Refpages/gl4/",
        "name": "OpenGL GLSL Reference Pages"
    },
    "threejs_shader_chunk": {
        "url": "https://github.com/mrdoob/three.js/blob/master/src/renderers/shaders/ShaderChunk.js",
        "name": "Three.js ShaderChunk Source"
    },
    "threejs_shader_lib": {
        "url": "https://github.com/mrdoob/three.js/blob/master/src/renderers/shaders/ShaderLib.js", 
        "name": "Three.js ShaderLib Source"
    },
    "threejs_uniforms_lib": {
        "url": "https://github.com/mrdoob/three.js/blob/master/src/renderers/shaders/UniformsLib.js",
        "name": "Three.js UniformsLib Source"
    },
    "threejs_uniforms_utils": {
        "url": "https://threejs.org/docs/#api/en/renderers/shaders/UniformsUtils",
        "name": "Three.js UniformsUtils Docs"
    },
    "onbeforecompile_guide": {
        "url": "https://medium.com/@pailhead011/extending-three-js-materials-with-glsl-78ea7bbb9270",
        "name": "Dusan Bosnjak - Extending Materials with GLSL"
    },
    "threejs_journey_modified": {
        "url": "https://threejs-journey.com/lessons/modified-materials",
        "name": "Three.js Journey - Modified Materials"
    },
    "codrops_marbles": {
        "url": "https://tympanus.net/codrops/2021/08/02/magical-marbles-in-three-js/",
        "name": "Codrops - Magical Marbles onBeforeCompile"
    },
    "threejs_modified_example": {
        "url": "https://threejs.org/examples/webgl_materials_modified.html",
        "name": "Three.js Official Modified Materials Example"
    }
}

def fetch_content(url: str) -> str:
    """Fetch and clean content from a URL"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text[:8000]  # Limit content length
        
    except Exception as e:
        return f"Error fetching content: {str(e)}"

@mcp.tool()
def search_glsl_fundamentals(topic: str) -> Dict:
    """Search GLSL fundamentals from Book of Shaders, OpenGL.org, Khronos, and WebGL resources
    
    Args:
        topic (str): GLSL topic to search for (e.g., "uniforms", "vertex shader", "fragment shader", "functions", "reference")
    
    Returns:
        dict: Relevant GLSL documentation and examples
    """
    
    results = {}
    
    # Book of Shaders - specific chapters based on topic
    if any(keyword in topic.lower() for keyword in ["uniform", "varying", "attribute", "basics"]):
        url = "https://thebookofshaders.com/03/"
        results["book_of_shaders_uniforms"] = {
            "source": "The Book of Shaders - Uniforms",
            "url": url,
            "content": fetch_content(url)
        }
    
    if any(keyword in topic.lower() for keyword in ["color", "fragment", "pixel"]):
        url = "https://thebookofshaders.com/02/"
        results["book_of_shaders_hello"] = {
            "source": "The Book of Shaders - Hello Fragment",
            "url": url,
            "content": fetch_content(url)
        }
    
    if any(keyword in topic.lower() for keyword in ["function", "shaping"]):
        url = "https://thebookofshaders.com/05/"
        results["book_of_shaders_functions"] = {
            "source": "The Book of Shaders - Shaping Functions",
            "url": url,
            "content": fetch_content(url)
        }
    
    # WebGL Fundamentals for technical details
    if any(keyword in topic.lower() for keyword in ["webgl", "glsl", "technical", "reference"]):
        results["webgl_fundamentals"] = {
            "source": DOCS_SITES["webgl_fundamentals"]["name"],
            "url": DOCS_SITES["webgl_fundamentals"]["url"],
            "content": fetch_content(DOCS_SITES["webgl_fundamentals"]["url"])
        }
    
    # Three.js Manual for shader basics
    if any(keyword in topic.lower() for keyword in ["threejs", "three", "manual", "basics"]):
        results["threejs_shaders"] = {
            "source": DOCS_SITES["threejs_manual_shaders"]["name"],
            "url": DOCS_SITES["threejs_manual_shaders"]["url"],
            "content": fetch_content(DOCS_SITES["threejs_manual_shaders"]["url"])
        }
    
    return results

@mcp.tool()
def search_r3f_shader_setup(topic: str) -> Dict:
    """Search React Three Fiber shader implementation guides
    
    Args:
        topic (str): R3F shader topic (e.g., "setup", "shaderMaterial", "uniforms", "vertex", "fragment")
    
    Returns:
        dict: R3F shader implementation tutorials and examples
    """
    
    results = {}
    
    # Always include the main R3F shader guide
    results["maxime_heckel_guide"] = {
        "source": DOCS_SITES["maxime_heckel_shaders"]["name"],
        "url": DOCS_SITES["maxime_heckel_shaders"]["url"],
        "content": fetch_content(DOCS_SITES["maxime_heckel_shaders"]["url"])
    }
    
    # Include Shadertoy conversion guides
    if any(keyword in topic.lower() for keyword in ["shadertoy", "convert", "port"]):
        results["shadertoy_conversion"] = {
            "source": DOCS_SITES["shadertoy_to_r3f"]["name"],
            "url": DOCS_SITES["shadertoy_to_r3f"]["url"],
            "content": fetch_content(DOCS_SITES["shadertoy_to_r3f"]["url"])
        }
        # Also include Three.js manual Shadertoy section
        results["threejs_shadertoy"] = {
            "source": DOCS_SITES["threejs_manual_shadertoy"]["name"],
            "url": DOCS_SITES["threejs_manual_shadertoy"]["url"],
            "content": fetch_content(DOCS_SITES["threejs_manual_shadertoy"]["url"])
        }
    
    # Include reveal effect tutorial
    if any(keyword in topic.lower() for keyword in ["effect", "reveal", "animation"]):
        results["codrops_reveal"] = {
            "source": DOCS_SITES["codrops_reveal"]["name"],
            "url": DOCS_SITES["codrops_reveal"]["url"],
            "content": fetch_content(DOCS_SITES["codrops_reveal"]["url"])
        }
    
    return results

@mcp.tool()
def search_particle_shaders(topic: str) -> Dict:
    """Search particle shader tutorials and GPU particle systems
    
    Args:
        topic (str): Particle topic (e.g., "gpu particles", "FBO", "curve", "trail", "buffer geometry")
    
    Returns:
        dict: Particle shader tutorials and implementation guides
    """
    
    results = {}
    
    # GPU Particles basics
    if any(keyword in topic.lower() for keyword in ["gpu", "basic", "setup", "floattype"]):
        results["gpu_particles_basic"] = {
            "source": DOCS_SITES["gpu_particles"]["name"],
            "url": DOCS_SITES["gpu_particles"]["url"],
            "content": fetch_content(DOCS_SITES["gpu_particles"]["url"])
        }
    
    # Advanced particles with FBO
    if any(keyword in topic.lower() for keyword in ["fbo", "advanced", "buffer", "frame"]):
        results["advanced_particles"] = {
            "source": DOCS_SITES["maxime_particles"]["name"],
            "url": DOCS_SITES["maxime_particles"]["url"],
            "content": fetch_content(DOCS_SITES["maxime_particles"]["url"])
        }
    
    # Curve-based particles
    if any(keyword in topic.lower() for keyword in ["curve", "path", "trail", "line"]):
        results["curve_particles"] = {
            "source": DOCS_SITES["curve_particles"]["name"],
            "url": DOCS_SITES["curve_particles"]["url"],
            "content": fetch_content(DOCS_SITES["curve_particles"]["url"])
        }
    
    return results

@mcp.tool()
def search_threejs_material_modification(topic: str) -> Dict:
    """Search advanced Three.js material modification with onBeforeCompile, ShaderChunk, and ShaderLib
    
    Args:
        topic (str): Material modification topic (e.g., "onBeforeCompile", "ShaderChunk", "material patching", "uniforms")
    
    Returns:
        dict: Advanced Three.js shader modification tutorials and source references
    """
    
    results = {}
    
    # Always include the definitive onBeforeCompile guide
    if any(keyword in topic.lower() for keyword in ["onbeforecompile", "before", "compile", "patch", "modify", "extend"]):
        results["onbeforecompile_guide"] = {
            "source": DOCS_SITES["onbeforecompile_guide"]["name"],
            "url": DOCS_SITES["onbeforecompile_guide"]["url"],
            "content": fetch_content(DOCS_SITES["onbeforecompile_guide"]["url"])
        }
        
        # Add Three.js Journey lesson
        results["threejs_journey_modified"] = {
            "source": DOCS_SITES["threejs_journey_modified"]["name"],
            "url": DOCS_SITES["threejs_journey_modified"]["url"],
            "content": fetch_content(DOCS_SITES["threejs_journey_modified"]["url"])
        }
        
        # Add practical example
        results["codrops_marbles"] = {
            "source": DOCS_SITES["codrops_marbles"]["name"],
            "url": DOCS_SITES["codrops_marbles"]["url"],
            "content": fetch_content(DOCS_SITES["codrops_marbles"]["url"])
        }
    
    # ShaderChunk and ShaderLib source references
    if any(keyword in topic.lower() for keyword in ["chunk", "shaderchunk", "lib", "shaderlib", "source"]):
        results["shader_chunk_source"] = {
            "source": DOCS_SITES["threejs_shader_chunk"]["name"],
            "url": DOCS_SITES["threejs_shader_chunk"]["url"],
            "content": f"Three.js ShaderChunk.js contains all shader chunk definitions used in built-in materials. View source: {DOCS_SITES['threejs_shader_chunk']['url']}"
        }
        
        results["shader_lib_source"] = {
            "source": DOCS_SITES["threejs_shader_lib"]["name"],
            "url": DOCS_SITES["threejs_shader_lib"]["url"],
            "content": f"Three.js ShaderLib.js contains shader programs for all built-in materials. View source: {DOCS_SITES['threejs_shader_lib']['url']}"
        }
    
    # Uniforms management
    if any(keyword in topic.lower() for keyword in ["uniform", "uniforms", "uniformslib", "uniformsutils"]):
        results["uniforms_lib_source"] = {
            "source": DOCS_SITES["threejs_uniforms_lib"]["name"],
            "url": DOCS_SITES["threejs_uniforms_lib"]["url"],
            "content": f"Three.js UniformsLib.js contains uniform definitions used across materials. View source: {DOCS_SITES['threejs_uniforms_lib']['url']}"
        }
        
        results["uniforms_utils_docs"] = {
            "source": DOCS_SITES["threejs_uniforms_utils"]["name"],
            "url": DOCS_SITES["threejs_uniforms_utils"]["url"],
            "content": fetch_content(DOCS_SITES["threejs_uniforms_utils"]["url"])
        }
    
    # Official example
    if any(keyword in topic.lower() for keyword in ["example", "demo", "modified"]):
        results["official_example"] = {
            "source": DOCS_SITES["threejs_modified_example"]["name"],
            "url": DOCS_SITES["threejs_modified_example"]["url"],
            "content": f"Official Three.js example showing material modification in action: {DOCS_SITES['threejs_modified_example']['url']}"
        }
    
    return results

@mcp.tool()
def get_all_shader_resources() -> Dict:
    """Get a comprehensive overview of all available shader resources
    
    Returns:
        dict: Complete list of all GLSL and R3F shader documentation sources
    """
    
    resources = {
        "glsl_fundamentals": {
            "The Book of Shaders": "https://thebookofshaders.com",
            "OpenGL.org": "https://www.opengl.org",
            "Khronos OpenGL": "https://www.khronos.org/opengl",
            "WebGL Fundamentals": DOCS_SITES["webgl_fundamentals"]["url"],
            "Three.js Manual - Shaders": DOCS_SITES["threejs_manual_shaders"]["url"]
        },
        "r3f_implementation": {
            "Maxime Heckel R3F Shaders": DOCS_SITES["maxime_heckel_shaders"]["url"],
            "Shadertoy to R3F Workflow": DOCS_SITES["shadertoy_to_r3f"]["url"],
            "Three.js Manual - Shadertoy": DOCS_SITES["threejs_manual_shadertoy"]["url"],
            "Codrops Shader Effects": DOCS_SITES["codrops_reveal"]["url"]
        },
        "particle_systems": {
            "GPU Particles Basics": DOCS_SITES["gpu_particles"]["url"],
            "Advanced Particles with FBO": DOCS_SITES["maxime_particles"]["url"],
            "Curve-based Particles": DOCS_SITES["curve_particles"]["url"]
        },
        "threejs_material_modification": {
            "onBeforeCompile Guide": DOCS_SITES["onbeforecompile_guide"]["url"],
            "Three.js Journey Modified Materials": DOCS_SITES["threejs_journey_modified"]["url"],
            "Codrops Magical Marbles": DOCS_SITES["codrops_marbles"]["url"],
            "ShaderChunk Source": DOCS_SITES["threejs_shader_chunk"]["url"],
            "ShaderLib Source": DOCS_SITES["threejs_shader_lib"]["url"],
            "UniformsLib Source": DOCS_SITES["threejs_uniforms_lib"]["url"],
            "UniformsUtils Docs": DOCS_SITES["threejs_uniforms_utils"]["url"],
            "Official Modified Example": DOCS_SITES["threejs_modified_example"]["url"]
        },
        "usage": {
            "description": "Use specific search functions for targeted results:",
            "functions": [
                "search_glsl_fundamentals() - GLSL basics, functions, uniforms, WebGL",
                "search_r3f_shader_setup() - React Three Fiber implementation, Shadertoy conversion",
                "search_particle_shaders() - GPU particles and advanced effects",
                "search_threejs_material_modification() - onBeforeCompile, ShaderChunk, material patching"
            ]
        },
        "total_sources": "22 comprehensive documentation sources"
    }
    
    return resources

if __name__ == "__main__":
    mcp.run()