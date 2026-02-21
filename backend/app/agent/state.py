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
    agent: str
    status: StepStatus = StepStatus.pending
    output: Dict[str, Any] = {}


class AgentState(BaseModel):
    build_id: str
    goal: str
    steps: List[AgentStep]
    current_step: int = 0
    completed: bool = False