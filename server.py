from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from langchain_community.utilities.arxiv import ArxivAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

mcp = FastMCP("crawler")


@mcp.tool()
def search_pubmed(query:str):
    arxiv = ArxivAPIWrapper(
        top_k_results=20,
        continue_on_failure=True
    )
    docs = arxiv.run(query=query)
    return docs


@mcp.tool()
def wiki_search(query:str):
    wiki = WikipediaAPIWrapper()
    res = wiki.run(query=query)
    return res



if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')