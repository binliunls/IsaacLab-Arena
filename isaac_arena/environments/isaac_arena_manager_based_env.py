# Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
#

from isaac_arena.embodiments.embodiment_base import ActionsCfg, EventCfg, ObservationsCfg
from isaac_arena.tasks.pick_and_place_task import TerminationsCfg
from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass

# TODO(alex.millane, 2025-07-23): Consider if we actually need this. What is missing from the base class?


@configclass
class IsaacArenaManagerBasedRLEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for an Isaac Arena environment."""

    # Scene settings
    scene: InteractiveSceneCfg

    observations: ObservationsCfg
    actions: ActionsCfg
    events: EventCfg

    terminations: TerminationsCfg

    # Unused managers
    commands = None
    rewards = None
    curriculum = None

    def __post_init__(self):
        """Post initialization."""
        # general settings
        self.decimation = 5
        self.episode_length_s = 30.0
        # simulation settings
        self.sim.dt = 0.01  # 100Hz
        self.sim.render_interval = 2
