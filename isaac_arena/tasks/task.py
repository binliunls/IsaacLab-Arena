from abc import ABC
from typing import Any, Dict

from isaac_arena.scene.scene import PickAndPlaceScene, SceneBase


class TaskBase(ABC):
    def __init__(self, scene: SceneBase):
        self.scene = scene

    def get_termination_cfg(self):
        pass

    def get_prompt(self) -> str:
        pass
