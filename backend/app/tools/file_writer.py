import os
from .registry import register_tool


BASE_PATH = "backend/generated_projects"


@register_tool("generate_backend")
async def generate_backend(state):
    project_path = os.path.join(BASE_PATH, state.build_id)
    os.makedirs(project_path, exist_ok=True)

    file_path = os.path.join(project_path, "main.py")

    with open(file_path, "w") as f:
        f.write("# Auto-generated backend\n")

    return {"files_created": ["main.py"]}


@register_tool("generate_frontend")
async def generate_frontend(state):
    project_path = os.path.join(BASE_PATH, state.build_id)
    file_path = os.path.join(project_path, "frontend.txt")

    with open(file_path, "w") as f:
        f.write("Frontend placeholder")

    return {"files_created": ["frontend.txt"]}


@register_tool("plan_project")
async def plan_project(state):
    return {"message": "Plan created"}


@register_tool("validate_project")
async def validate_project(state):
    return {"message": "Validation passed"}