from crewai import Crew, Process
from agents import planner_agent, researcher_agent, analyst_agent, critic_agent
from tasks import planning_task, research_task, analysis_task, critique_task


crew = Crew(
    agents=[
        planner_agent,
        researcher_agent,
        analyst_agent,
        critic_agent
    ],
    tasks=[
        planning_task,
        research_task,
        analysis_task,
        critique_task
    ],
    process=Process.sequential,
    verbose=True
)


if __name__ == "__main__":

    result = crew.kickoff(
        inputs={
            "topic": "Emerging GenAI use cases in FMCG supply chains"
        }
    )

    print("\nFINAL REPORT\n")
    print(result)