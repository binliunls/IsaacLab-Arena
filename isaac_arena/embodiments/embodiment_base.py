from abc import ABC
from typing import Any

from isaaclab.utils import configclass


@configclass
class ActionsCfg:
    pass


@configclass
class ObservationsCfg:
    pass


@configclass
class EventCfg:
    pass


class EmbodimentBase(ABC):

    # FIX: This is wrong. These are class variables.
    scene_config: Any | None = None
    action_config: ActionsCfg | None = None
    observation_config: ObservationsCfg | None = None
    event_config: EventCfg | None = None

    def __init__(self):
        pass

    def get_scene_cfg(self) -> Any:
        return self.scene_config

    def get_action_cfg(self) -> Any:
        return self.action_config

    def get_observation_cfg(self) -> Any:
        return self.observation_config

    def get_event_cfg(self) -> Any:
        return self.event_config
