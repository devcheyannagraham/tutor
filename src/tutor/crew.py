from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from tutor.worksheet import create_worksheet

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Tutor():
    """Tutor crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def tutor(self) -> Agent:
        return Agent(
            config=self.agents_config['tutor'], # type: ignore[index]
            # verbose=True
        )
    
    @task
    def tutor_task(self) -> Task:
        return Task(
            config=self.tasks_config['tutor_task'], # type: ignore[index]
            verbose=True,
            tools=[create_worksheet] # Adding the worksheet creation tool to the task
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Tutor crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
