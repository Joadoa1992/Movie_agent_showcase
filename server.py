import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MovieWrapper")

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/movie-hybrid-rag"

@mcp.tool()
def search_movies_hybrid_rag(query: str) -> str:
    """Search the Neo4j movie database via n8n webhook.
    
    Args:
        query: Movie description, genre, or search prompt string.
    """
    if not query or not query.strip():
        return "Error: No search query provided."

    payload = {"query": query}

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=120)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"n8n request failed: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")