from abc import ABC


class TaskBase(ABC):

    def get_termination_cfg(self):
        pass

    def get_prompt(self) -> str:
        pass
