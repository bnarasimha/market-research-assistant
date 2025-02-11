from crewai import Agent, Task
from openai import OpenAI
from crewai_tools import ScrapeWebsiteTool
from pydantic import BaseModel, Field

class CompetitorInfo(BaseModel):
    info: str = Field(..., description="Detailed information about GitHub Copilot and Cursor features and capabilities")

competitor_analyst = Agent(
            role='Competitor Analyst',
            goal="""Research and gather detailed information about GitHub Copilot and Cursor.
            Gather below information about the products:
            1. Intelligent Code Generation
            2. Integration Capabilities
            3. Natural Language Interface
            4. User Experience
            5. Pricing and Licensing
            6. Community and Support
            7. Security and Privacy
            8. Scalability and Performance
            9. Documentation and Learning Resources
            10. Future Development and Roadmap""",
            backstory='Expert at analyzing product features and capabilities using AI platforms',
            expected_output='Detailed information about GitHub Copilot and Cursor features and capabilities',
            output_pydantic=CompetitorInfo,
            tools=[ScrapeWebsiteTool(name="Scrape Website Tool", description="Use this tool to scrape the website of GitHub Copilot and Cursor")]
        )

competitor_research_task = Task(
    description="Research and gather detailed information about GitHub Copilot and Cursor",
    expected_output="Detailed information about GitHub Copilot and Cursor features and capabilities",
    agent=competitor_analyst
)