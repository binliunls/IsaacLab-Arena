


#%%


import gymnasium as gym
import tqdm
import torch

# Launching the simulation app
from isaaclab.app import AppLauncher
import pinocchio # THERE IS AN ISSUE HERE THAT WE REQUIRE THIS.
print("Launching simulation app once in notebook")
simulation_app = AppLauncher()


from isaac_arena.cli.isaac_arena_cli import get_isaac_arena_cli_parser
from isaac_arena.assets.asset_registry import AssetRegistry
from isaac_arena.embodiments.franka import FrankaEmbodiment
from isaac_arena.scene.pick_and_place_scene import PickAndPlaceScene
from isaac_arena.tasks.pick_and_place_task import PickAndPlaceTask
from isaac_arena.environments.compile_env import ArenaEnvBuilder
from isaac_arena.environments.isaac_arena_environment import IsaacArenaEnvironment
from isaac_arena.geometry.pose import Pose

from isaac_arena.fixures.fixtures import Microwave

# NEW
from isaac_arena.scene.open_door_scene import OpenDoorScene
from isaac_arena.tasks.open_door import OpenDoorTask


args_parser = get_isaac_arena_cli_parser()
# args_cli = args_parser.parse_args([])
args_cli = args_parser.parse_args([])


asset_registry = AssetRegistry()
background = asset_registry.get_asset_by_name("packing_table_pick_and_place")()
object = asset_registry.get_asset_by_name("microwave")()
# object = asset_registry.get_asset_by_name("cracker_box")()

# Put the microwave on the packing table.
object.set_initial_pose(Pose(
    position_xyz=(0.6, -0.00586, 0.22773),
    rotation_wxyz=(0.7071068, 0, 0, -0.7071068),
))

isaac_arena_environment = IsaacArenaEnvironment(
    name="open_door",
    embodiment=FrankaEmbodiment(),
    scene=OpenDoorScene(background, object),
    task=OpenDoorTask(),
)

env_builder = ArenaEnvBuilder(isaac_arena_environment, args_cli)
name, cfg = env_builder.build_registered()
print(f"Building env with name: {name}")
env = gym.make(name, cfg=cfg)
env.reset()

# Run some zero actions.
NUM_STEPS = 100000
for _ in tqdm.tqdm(range(NUM_STEPS)):
    with torch.inference_mode():
        actions = torch.zeros(env.action_space.shape, device=env.unwrapped.device)
        env.step(actions)














#%%