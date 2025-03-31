from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import language_tool_python

class AcademicGrammarCheckerInput(BaseModel):
    """Input schema for AcademicGrammarChecker."""
    text: str = Field(..., description="Text to check for grammar and style issues.")

class AcademicGrammarChecker(BaseTool):
    name: str = "Academic Grammar Checker"
    description: str = (
        "This tool checks the provided text for grammar and style issues."
    )
    args_schema: Type[BaseModel] = AcademicGrammarCheckerInput

    def _run(self, text: str) -> str:
        tool = language_tool_python.LanguageTool("en-US")
        matches = tool.check(text)
        return tool.correct(text)