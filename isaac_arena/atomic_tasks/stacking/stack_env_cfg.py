
@configclass
class SceneCfg(InteractiveSceneCfg):
    # For now lets assume this always contains a list of 
    # manipulatable objects, scene objects, a background scene and a text description

    background_scene = AssetBaseCfg()

    manipulatable_objects = List[AssetBaseCfg]

    scene_objects = List[AssetBaseCfg]

    robot: AssetBaseCfg()

    task_description = "Stack all the manipulatable objects on top of each other"


@configclass
class ObservationsCfg:
    @configclass
    class RobotObs(ObsGroup):
        robot_observation = self.robot.get_obs()


@configclass
class StackEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for the stacking environment."""

    # Scene settings
    # This is task specific
    scene: SceneCfg = SceneCfg(num_envs=4096, env_spacing=2.5, replicate_physics=False)
    # This can also be task specific
    observations: ObservationsCfg = ObservationsCfg()
    # This is robot specific
    actions = None
    # This is manipulatable object specific
    terminations: TerminationsCfg = TerminationsCfg()

    # Unused managers
    commands = None
    rewards = None
    events = None
    curriculum = None


    def __post_init__(self):
        """Post initialization."""
        # general physics settings
        self.decimation = 5
        self.episode_length_s = 30.0
        # simulation settings
        self.sim.dt = 0.01  # 100Hz
        self.sim.render_interval = 2

        self.sim.physx.bounce_threshold_velocity = 0.2
        self.sim.physx.bounce_threshold_velocity = 0.01
        self.sim.physx.gpu_found_lost_aggregate_pairs_capacity = 1024 * 1024 * 4
        self.sim.physx.gpu_total_aggregate_pairs_capacity = 16 * 1024
        self.sim.physx.friction_correlation_distance = 0.00625