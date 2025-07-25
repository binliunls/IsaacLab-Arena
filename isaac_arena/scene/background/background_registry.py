from isaac_arena.scene.background.background import Background, Kitchen

BACKGROUND_REGISTRY = {
    "kitchen": Kitchen,
    # add more backgrounds here…
}


def get_background(name: str, **kwargs) -> Background:
    try:
        cls = BACKGROUND_REGISTRY[name]
    except KeyError:
        raise ValueError(f"No background-scene named {name!r}")
    return cls(**kwargs)
