from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import PyPDF2

class PDFTextExtractorInput(BaseModel):
    """Input schema for PDFTextExtractor."""
    file_path: str = Field(..., description="Path to the PDF file to extract text from.")

class PDFTextExtractor(BaseTool):
    name: str = "PDF Text Extractor"
    description: str = (
        "This tool extracts text from a PDF file."
    )
    args_schema: Type[BaseModel] = PDFTextExtractorInput

    def _run(self, file_path: str) -> str:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extractText()
        return text