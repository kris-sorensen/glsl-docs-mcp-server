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
- `get_all_shader_resources()` - Complete resource list

## Documentation Sources

1. **The Book of Shaders** - https://thebookofshaders.com/
2. **OpenGL.org** - https://www.opengl.org/
3. **Khronos OpenGL** - https://www.khronos.org/opengl/
4. **Maxime Heckel R3F Guide** - Shader setup tutorial
5. **TheFrontDev Shadertoy to R3F** - Conversion workflow
6. **Codrops Reveal Effect** - Practical shader effects
7. **TheFrontDev GPU Particles** - Particle basics
8. **Maxime Heckel Advanced Particles** - FBO techniques
9. **TheFrontDev Curve Particles** - Trail effects

## Contributing

To add new documentation sources:

1. Add the site to `DOCS_SITES` in `server.py`
2. Create/update relevant search functions
3. Test the new content
4. Submit a pull request

## License

MIT License