from dataclasses import MISSING
from typing import Any

from isaac_arena.geometry.pose import Pose
from isaac_arena.scene.scene import SceneBase
from isaaclab.assets import AssetBaseCfg, RigidObjectCfg
from isaaclab.assets.articulation.articulation_cfg import ArticulationCfg
from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg
from isaaclab.utils import configclass


@configclass
class PickAndPlaceSceneCfg:

    # The scene of the environment where the task is performed
    background_scene: AssetBaseCfg = MISSING

    # The object to pick up
    pick_up_object: RigidObjectCfg = MISSING

    # The object to place the pick_up_object on/into
    destination_object: RigidObjectCfg = MISSING


class KitchenPickAndPlaceScene(SceneBase):
    def __init__(
        self, pick_up_object: RigidObjectCfg, destination_object: RigidObjectCfg, robot: ArticulationCfg = None
    ):
        super().__init__()
        # The background scene
        self.background_scene = AssetBaseCfg(
            prim_path="{ENV_REGEX_NS}/Kitchen",
            # These positions are hardcoded for the kitchen scene. Its important to keep them.
            init_state=AssetBaseCfg.InitialStateCfg(pos=[0.772, 3.39, -0.895], rot=[0.70711, 0, 0, -0.70711]),
            spawn=UsdFileCfg(
                usd_path="omniverse://isaac-dev.ov.nvidia.com/Projects/nvblox/isaac_arena/kitchen_scene_teleop_v3.usd"
            ),
        )
        # An object, which has to be placed on/into the target object
        self.pick_up_object: RigidObjectCfg = pick_up_object

        # An object, which has to be placed on/into the target object
        self.destination_object: RigidObjectCfg = destination_object

        # Robot configuration
        self.robot: ArticulationCfg = robot

        # The position of the robot
        self.robot_initial_pose = Pose.identity()

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


class MugInDrawerKitchenPickAndPlaceScene(KitchenPickAndPlaceScene):
    def __init__(self, robot: ArticulationCfg = None):
        super().__init__(
            pick_up_object=RigidObjectCfg(
                prim_path="{ENV_REGEX_NS}/target_mug",
                init_state=RigidObjectCfg.InitialStateCfg(pos=[0.35, 0.0, 0.094], rot=[0.0, 0.0, 0.0, 1.0]),
                spawn=UsdFileCfg(
                    usd_path=(
                        "omniverse://isaac-dev.ov.nvidia.com/Projects/nvblox/Collected_kitchen_scene/mug_physics.usd"
                    ),
                    scale=(0.0125, 0.0125, 0.0125),
                    activate_contact_sensors=True,
                ),
            ),
            # NOTE(alexmillane, 2025-07-28): We used to have a dummy object placed on the bottom of the drawer to
            # serve as a destination object. Now I just reference the cabinet. This hasn't yet been tested. So this
            # will need some work to make this actually functional.
            destination_object=RigidObjectCfg(prim_path="{ENV_REGEX_NS}/Kitchen/Cabinet_B_02"),
            robot=robot,
        )
