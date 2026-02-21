from fastapi import APIRouter, WebSocket
from app.agent.state import AgentState
from app.agent.planner import create_plan
from app.agent.agent import AutoDevAgent
from app.services.websocket_manager import ConnectionManager
import uuid

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)


@router.post("/build")
async def create_build(goal: str):

    build_id = str(uuid.uuid4())

    steps = create_plan(goal)

    state = AgentState(
        build_id=build_id,
        goal=goal,
        steps=steps
    )

    agent = AutoDevAgent(state, manager.broadcast)

    import asyncio
    asyncio.create_task(agent.run())

    return {"build_id": build_id}