from crewai import Agent
from config import llm
from tools import get_search_tool

search_tool = get_search_tool()


planner_agent = Agent(
    role="AI Research Planner",
    goal="Break the research problem into structured subtasks",
    backstory=(
        "You are an expert research planner who specializes in breaking "
        "complex analytical problems into clear research steps. "
        "You help AI systems structure investigations efficiently."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=True
)


researcher_agent = Agent(
    role="AI Market Researcher",
    goal="Find emerging Generative AI use cases in FMCG supply chains",
    backstory=(
        "You are a technology market researcher with expertise in supply chain "
        "innovation, AI adoption, and FMCG industry trends. "
        "You gather reliable insights from the web and summarize them clearly."
    ),
    tools=[search_tool],
    llm=llm,
    verbose=True
)


analyst_agent = Agent(
    role="Supply Chain AI Analyst",
    goal="Generate a structured report explaining GenAI use cases in FMCG supply chains",
    backstory=(
        "You are a strategic analyst specializing in supply chain transformation "
        "through artificial intelligence. You analyze research findings and "
        "convert them into structured business insights."
    ),
    llm=llm,
    verbose=True
)


critic_agent = Agent(
    role="AI Research Critic",
    goal="Review the generated report and improve its quality",
    backstory=(
        "You are a senior AI consultant responsible for reviewing analytical "
        "reports and identifying missing insights, weak reasoning, or possible "
        "hallucinations. You ensure the final report is accurate and well structured."
    ),
    llm=llm,
    verbose=True
)