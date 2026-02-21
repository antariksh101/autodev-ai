from .state import StepStatus
from app.tools.registry import TOOLS


class AutoDevAgent:

    def __init__(self, state, broadcaster):
        self.state = state
        self.broadcast = broadcaster

    async def run(self):
        for step in self.state.steps:

            step.status = StepStatus.running
            await self.broadcast(self.state.dict())

            try:
                tool = TOOLS.get(step.tool)
                result = await tool(self.state)

                step.result = result
                step.status = StepStatus.completed

            except Exception as e:
                step.status = StepStatus.failed
                step.result = {"error": str(e)}
                break

            await self.broadcast(self.state.dict())

        self.state.completed = True
        await self.broadcast(self.state.dict())