from typing import Any

from emp_agents import AgentBase, GenericTool
from emp_agents.models import AssistantMessage, UserMessage
from pydantic import PrivateAttr
import yaml

from .tools import get_current_time

PROMPT_PATH = "./demo_agent/prompts.yaml"


class DemoAgent(AgentBase):
    _config: dict[str, Any] = PrivateAttr()
    use_conversation_history: bool = True

    def model_post_init(self, __context: Any) -> None:
        with open(PROMPT_PATH) as f:
            self._config = yaml.safe_load(f)
        self.prompt = self._config["system prompt"]
        super().model_post_init(__context)

        if self.use_conversation_history:
            self._load_conversation_history()

    def _load_conversation_history(self) -> None:
        conversation = self._config["conversation history"]
        for message in conversation:
            if message.startswith("user:"):
                self.conversation_history.append(
                    UserMessage(content=message.lstrip("user: "))
                )
            elif message.startswith("assistant:"):
                self.conversation_history.append(
                    AssistantMessage(content=message.lstrip("assistant: "))
                )

    tools: list[GenericTool] = [
        GenericTool.from_func(get_current_time),
    ]
