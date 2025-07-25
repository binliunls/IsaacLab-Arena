from isaaclab.assets import RigidObjectCfg
from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg


class PickUpObjects:
    """
    Encapsulates the pick-up object config for a pick-and-place environment.
    """

    def __init__(self, pick_up_object: RigidObjectCfg):
        self.pick_up_object = pick_up_object

    def get_pick_up_object(self) -> RigidObjectCfg:
        """Return the configured pick-up object asset."""
        return self.pick_up_object


class Mug(PickUpObjects):
    """
    Encapsulates the pick-up object config for a pick-and-place environment.
    """

    def __init__(self):
        super().__init__(
            RigidObjectCfg(
                prim_path="{ENV_REGEX_NS}/target_mug",
                init_state=RigidObjectCfg.InitialStateCfg(pos=[0.35, 0.0, 0.094], rot=[0.0, 0.0, 0.0, 1.0]),
                spawn=UsdFileCfg(
                    usd_path=(
                        "omniverse://isaac-dev.ov.nvidia.com/Projects/nvblox/Collected_kitchen_scene/mug_physics.usd"
                    ),
                    scale=(0.0125, 0.0125, 0.0125),
                    activate_contact_sensors=True,
                ),
            )
        )
