from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import matplotlib.pyplot as plt
import io
import base64


class DataVisualizerInput(BaseModel):
    """Input schema for DataVisualizer."""
    data: dict = Field(..., description="Data to visualize as a graph.")


class DataVisualizer(BaseTool):
    name: str = "Data Visualizer"
    description: str = (
        "This tool creates visualizations from the provided data."
    )
    args_schema: Type[BaseModel] = DataVisualizerInput

    def _run(self, data: dict) -> str:
        fig, ax = plt.subplots()
        ax.plot(data["x"], data["y"])
        ax.set(xlabel='X-axis', ylabel='Y-axis', title='Data Visualization')
        ax.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        return img_str