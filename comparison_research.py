from crewai import Agent, Task
from pydantic import BaseModel, Field


class ComparisonReport(BaseModel):
    comparison_criteria: str = Field(..., description="Comparison criteria for Product Narsi and competitors")
    comparison_result: dict = Field(..., description="Comparison result for Product Narsi and competitors")

comparison_analyst = Agent(
            role="Comparison Analyst",
            goal=f"""Compare Product Narsi and competitors.
            Give the comparison on below categories:
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
            backstory="Expert at analyzing product features and capabilities using AI platforms. You have information about Product Narsi and competitors",
        )

comparison_research_task = Task(
    description="Compare and analyze Product Narsi and competitors",
    agent=comparison_analyst,
    expected_output="""Detailed information about Product Narsi and competitors features and capabilities in a table format.
            You must return a list of comparisons where each comparision contains:
            - category : category the comparison is about
            - Narsi : rating of Product Narsi on the category
            - GitHub Copilot : rating of GitHub Copilot on the category
            - Cursor : rating of Cursor on the category

            Example Output:
            {
                "comparison": [
                    {
                        "category": "Ease of Use",
                        "Narsi": "High",
                        "GitHub Copilot": "Very High",
                        "Cursor": "Moderate"
                    },
                    {
                        "category": "Code Suggestions",
                        "Narsi": "Accurate and Contextual",
                        "GitHub Copilot": "Highly Accurate",
                        "Cursor": "Moderate Accuracy"
                    },
                    #more categories
                ]
            }
            """
)