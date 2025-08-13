# Contributing to GLSL Docs MCP Server

Thank you for your interest in contributing! This guide will help you add new documentation sources and improve the server.

## Adding New Documentation Sources

### 1. Add to DOCS_SITES Dictionary

In `server.py`, add your new source to the `DOCS_SITES` dictionary:

```python
DOCS_SITES = {
    # ... existing sites ...
    "your_new_site": {
        "url": "https://example.com/glsl-tutorial",
        "name": "Your New GLSL Tutorial"
    }
}
```

### 2. Update Search Functions

Add your new site to relevant search functions:

```python
@mcp.tool()
def search_glsl_fundamentals(topic: str) -> Dict:
    # ... existing code ...
    
    # Add new condition for your site
    if any(keyword in topic.lower() for keyword in ["your", "keywords"]):
        results["your_new_content"] = {
            "source": DOCS_SITES["your_new_site"]["name"],
            "url": DOCS_SITES["your_new_site"]["url"],
            "content": fetch_content(DOCS_SITES["your_new_site"]["url"])
        }
```

### 3. Create New Search Categories (Optional)

For major new categories, create a new tool function:

```python
@mcp.tool()
def search_new_category(topic: str) -> Dict:
    """Search your new category of documentation
    
    Args:
        topic (str): Topic to search for
    
    Returns:
        dict: Relevant documentation from your new category
    """
    # Implementation here
```

## Testing Your Changes

1. **Local Testing:**
   ```bash
   # Test the server directly
   python server.py
   
   # Test with Claude Code
   # Restart Claude Code and try your new functions
   ```

2. **Validate URLs:**
   ```python
   # Test that your URLs are accessible
   import requests
   response = requests.get("https://your-new-site.com")
   print(response.status_code)  # Should be 200
   ```

## Submission Guidelines

### Pull Request Process

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b add-webgl2-docs
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Update README.md** if adding new categories
6. **Commit with descriptive messages:**
   ```bash
   git commit -m "Add WebGL2 documentation from khronos.org"
   ```
7. **Push and create Pull Request**

### Commit Message Format

- `feat: add new documentation source for WebGL2`
- `fix: improve content parsing for mobile sites`
- `docs: update README with new search functions`
- `refactor: optimize content fetching performance`

### What to Include

- **URL validation** - Ensure all URLs are accessible
- **Content quality** - Verify the fetched content is useful
- **Documentation** - Update README.md with new sources
- **Testing** - Test all search functions work correctly

## Code Style

- Follow existing code patterns
- Use descriptive variable names
- Add docstrings to new functions
- Keep functions focused and single-purpose
- Limit fetched content to reasonable sizes (8000 chars max)

## Common Issues

### Content Fetching Problems
- Some sites block scrapers - add appropriate headers
- JavaScript-heavy sites may need different approaches
- Rate limiting - add delays between requests if needed

### Site Structure Changes
- Websites change their HTML structure
- Test periodically and update selectors as needed
- Consider multiple fallback strategies

## Ideas for Contributions

### High Priority
- **Three.js official documentation**
- **WebGL2 reference materials**
- **Shader debugging tools**
- **Performance optimization guides**

### Medium Priority
- **Additional R3F libraries (Drei, etc.)**
- **Shader math/physics references**
- **Game development shader tutorials**
- **Mobile GPU considerations**

### Enhancement Ideas
- **Caching system** for frequently accessed content
- **Content categorization** improvements
- **Search result ranking** by relevance
- **API rate limiting** and error handling

## Questions?

Open an issue or start a discussion if you have questions about contributing!