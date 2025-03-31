from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class CrossrefCitationToolInput(BaseModel):
    """Input schema for CrossrefCitationTool."""
    doi: str = Field(..., description="DOI of the article to fetch citation.")

class CrossrefCitationTool(BaseTool):
    name: str = "Crossref Citation Tool"
    description: str = (
        "This tool fetches citation details from Crossref based on the provided DOI."
    )
    args_schema: Type[BaseModel] = CrossrefCitationToolInput

    def _run(self, doi: str) -> str:
        url = f"https://api.crossref.org/works/{doi}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["message"]["reference"]
        else:
            return "Error: Unable to fetch citation data from Crossref."