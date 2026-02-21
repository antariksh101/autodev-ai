from enum import Enum
from pydantic import BaseModel
from typing import List, Dict, Any


class StepStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class AgentStep(BaseModel):
    id: int
    name: str
    tool: str
    status: StepStatus = StepStatus.pending
    result: Dict[str, Any] = {}


class AgentState(BaseModel):
    build_id: str
    goal: str
    steps: List[AgentStep]
    completed: bool = False