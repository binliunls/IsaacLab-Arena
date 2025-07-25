from isaac_arena.scene.pick_up_object.pick_up_objects import Mug, PickUpObjects

PICKUP_REGISTRY = {
    "mug": Mug,
    # add more pickup-objects here…
}


def get_pickup_object(name: str, **kwargs) -> PickUpObjects:
    try:
        cls = PICKUP_REGISTRY[name]
    except KeyError:
        raise ValueError(f"No pick-up object named {name!r}")
    return cls(**kwargs)
