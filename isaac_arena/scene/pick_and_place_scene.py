from dataclasses import MISSING
from typing import Any

from isaac_arena.scene.scene import SceneBase
from isaaclab.assets import AssetBaseCfg, RigidObjectCfg
from isaaclab.utils import configclass


@configclass
class PickAndPlaceSceneCfg:

    # The scene of the environment where the task is performed
    background_scene: AssetBaseCfg = MISSING

    # The object to pick up
    pick_up_object: RigidObjectCfg = MISSING

    # The object to place the pick_up_object on/into
    destination_object: RigidObjectCfg = MISSING


class PickAndPlaceScene(SceneBase):
    def __init__(
        self, background_scene: AssetBaseCfg, pick_up_object: RigidObjectCfg, destination_object: RigidObjectCfg
    ):
        super().__init__()
        # The background scene
        self.background_scene = background_scene
        # An object, which has to be placed on/into the target object
        self.pick_up_object = pick_up_object

        # An object, which has to be placed on/into the target object
        self.destination_object = destination_object

    def get_scene_cfg(self) -> PickAndPlaceSceneCfg:
        return PickAndPlaceSceneCfg(
            background_scene=self.background_scene,
            pick_up_object=self.pick_up_object,
            destination_object=self.destination_object,
        )

    def get_observation_cfg(self) -> Any:
        pass

    def get_events_cfg(self) -> Any:
        pass
