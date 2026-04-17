# Tutor Crew

A crewAI-powered math tutoring assistant that helps students understand and complete their homework. Given a math problem, the AI tutor (modeled as a fifth-grade math teacher) explains how to solve the problem step-by-step, then generates 5 similar practice problems with solutions to reinforce the student's understanding.

Output is saved to `tutor_output.md`.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/tutor/config/agents.yaml` to define your agents
- Modify `src/tutor/config/tasks.yaml` to define your tasks
- Modify `src/tutor/crew.py` to add your own logic, tools and specific args
- Modify `src/tutor/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the tutor Crew, assembling the agents and assigning them tasks as defined in your configuration.

This command initializes the Tutor Crew with a math problem (set via the `problem` variable in `main.py`) and saves the tutoring output to `tutor_output.md`.

## Understanding Your Crew

The Tutor Crew uses a single AI agent — a fifth-grade math teacher — that receives a homework problem and produces:
1. A step-by-step explanation of how to solve the problem
2. Five similar practice problems with solutions

The problem to solve is configured via the `problem` variable in `src/tutor/main.py`. Agent and task behavior is defined in `config/agents.yaml` and `config/tasks.yaml`.

## Support

For support, questions, or feedback regarding the Tutor Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
