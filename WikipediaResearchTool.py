from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class WikipediaResearchToolInput(BaseModel):
    """Input schema for WikipediaResearchTool."""
    topic: str = Field(..., description="Topic to research on Wikipedia.")

class WikipediaResearchTool(BaseTool):
    name: str = "Wikipedia Research Tool"
    description: str = (
        "This tool fetches data from Wikipedia based on the provided topic."
    )
    args_schema: Type[BaseModel] = WikipediaResearchToolInput

    def _run(self, topic: str) -> str:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["extract"]
        else:
            return "Error: Unable to fetch data from Wikipedia."