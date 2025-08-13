# GLSL Docs MCP Server

A comprehensive MCP server for GLSL shader development with React Three Fiber.

## Features

- **GLSL Fundamentals**: The Book of Shaders, OpenGL.org, Khronos OpenGL
- **R3F Implementation**: Maxime Heckel guides, Shadertoy conversion, Codrops effects
- **Particle Systems**: GPU particles, FBO techniques, curve-based effects

## Installation

### Prerequisites
- Python 3.10+
- Claude Code or Claude Desktop

### Setup
```bash
git clone https://github.com/yourusername/glsl-docs-mcp.git
cd glsl-docs-mcp
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

**For Claude Code**, add to `~/.claude.json`:
```json
{
  "mcpServers": {
    "glsl_docs": {
      "command": "/path/to/glsl-docs-mcp/run_server.sh",
      "args": []
    }
  }
}
```

**For Claude Desktop**, add to config file:
```json
{
  "mcpServers": {
    "glsl_docs": {
      "command": "python",
      "args": ["/path/to/glsl-docs-mcp/server.py"]
    }
  }
}
```

## Usage

- `search_glsl_fundamentals("uniforms")` - GLSL basics and theory
- `search_r3f_shader_setup("shaderMaterial")` - R3F implementation
- `search_particle_shaders("gpu particles")` - Particle systems
- `search_threejs_material_modification("onBeforeCompile")` - Advanced material patching
- `get_all_shader_resources()` - Complete resource list

## Documentation Sources

### GLSL Fundamentals
1. **The Book of Shaders** - https://thebookofshaders.com/
2. **OpenGL.org** - https://www.opengl.org/
3. **Khronos OpenGL** - https://www.khronos.org/opengl/
4. **WebGL Fundamentals** - https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html
5. **Three.js Manual - Shaders** - https://threejs.org/manual/#en/shaders

### R3F Implementation
6. **Maxime Heckel R3F Guide** - Complete shader setup tutorial
7. **TheFrontDev Shadertoy to R3F** - Conversion workflow
8. **Three.js Manual - Shadertoy** - https://threejs.org/manual/#en/shadertoy
9. **Codrops Reveal Effect** - Practical shader effects

### Particle Systems
10. **TheFrontDev GPU Particles** - Particle basics
11. **Maxime Heckel Advanced Particles** - FBO techniques
12. **TheFrontDev Curve Particles** - Trail effects

### Advanced Three.js Material Modification
13. **Dusan Bosnjak - Extending Materials with GLSL** - The definitive onBeforeCompile guide
14. **Three.js Journey - Modified Materials** - Comprehensive material modification lesson
15. **Codrops - Magical Marbles** - Practical onBeforeCompile examples
16. **Three.js ShaderChunk Source** - All shader chunk definitions
17. **Three.js ShaderLib Source** - Built-in material shader programs
18. **Three.js UniformsLib Source** - Uniform definitions
19. **Three.js UniformsUtils Docs** - Uniform utilities API
20. **Official Modified Materials Example** - Live demo

**Total: 22 comprehensive documentation sources**

## Contributing

To add new documentation sources:

1. Add the site to `DOCS_SITES` in `server.py`
2. Create/update relevant search functions
3. Test the new content
4. Submit a pull request

## License

MIT License