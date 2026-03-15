from crewai import Task
from agents import planner_agent, researcher_agent, analyst_agent, critic_agent


planning_task = Task(
    description="""
Break down the research objective into subtasks.

Goal:
Identify the top 5 emerging GenAI use cases in FMCG supply chains.

Return the research steps required.
""",
    expected_output="A structured list of research subtasks",
    agent=planner_agent
    
)


research_task = Task(
    description="""
Research emerging GenAI applications in FMCG supply chains.

Focus on use cases such as:
- demand forecasting
- inventory optimization
- supplier risk prediction
- logistics route planning
- procurement automation

Use web search to gather insights.
""",
    expected_output="Detailed research notes describing GenAI supply chain use cases",
    agent=researcher_agent
)


analysis_task = Task(
    description="""
Create a structured report based on research findings.

For each of the top 5 GenAI use cases include:

1. Use Case Name
2. Implementation Approach
3. Expected Impact
4. Risks
5. Maturity Level
""",
    expected_output="A structured report describing 5 GenAI use cases in FMCG supply chains",
    agent=analyst_agent
)


critique_task = Task(
    description="""
Review the generated report and improve it.

Check for:
- missing insights
- weak explanations
- hallucinated claims

Provide a corrected version.
""",
    expected_output="An improved and validated final report",
    agent=critic_agent
)