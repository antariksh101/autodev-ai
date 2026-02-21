from .state import AgentStep


def create_plan(goal: str):
    return [
        AgentStep(id=1, name="Planning", tool="plan_project"),
        AgentStep(id=2, name="Generate Backend", tool="generate_backend"),
        AgentStep(id=3, name="Generate Frontend", tool="generate_frontend"),
        AgentStep(id=4, name="Validate Project", tool="validate_project"),
    ]