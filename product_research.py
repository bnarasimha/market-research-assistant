from crewai import Agent, Task
from openai import OpenAI
from crewai.tools import tool
from pydantic import BaseModel, Field
import os
class ProductNarsiInfo(BaseModel):
    info: str = Field(..., description="Detailed information about Product Narsi features and capabilities")

@tool("Product Research Tool")
def ProductResearchTool() -> str:
    """
    Fetches the information about Product Narsi from the GenAI Platform
    Args:
        None

    Returns:
        str: The information about Product Narsi.
    """

    agent_endpoint = os.getenv("GENAI_PRODUCT_RESEARCHER_AGENT_ENDPOINT")
    agent_key = os.getenv("GENAI_PRODUCT_RESEARCHER_AGENT_KEY")

    client = OpenAI(
        base_url = agent_endpoint,
        api_key = agent_key,
    )

    response = client.chat.completions.create(
        model = "DeepSeek R1 Distill Llama 70B",
        messages = [{"role": "user", "content": "You are an expert Product Researcher.  You are expert at analyzing product features and capabilities using AI platforms. Your task is to Research and gather detailed information about Product Narsi whose details will be available to you."}],
    )

    return response.choices[0].message.content
    

product_researcher = Agent(
    role="Product Researcher",
    goal="""Research and gather detailed information about Product Narsi.""",
    backstory="Expert at analyzing product features and capabilities using AI platforms",
    tools=[ProductResearchTool],
    verbose=True
)

product_research_task = Task(
    description="Research and gather detailed information about Product Narsi",
    expected_output="Detailed information about Product Narsi features and capabilities",
    agent=product_researcher,
    output_pydantic=ProductNarsiInfo,
    verbose=True
)