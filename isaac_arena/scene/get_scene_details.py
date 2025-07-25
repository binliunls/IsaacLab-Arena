# Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
#

from isaac_arena.scene.background.background_registry import get_background
from isaac_arena.scene.pick_up_object.pick_up_object_registry import get_pickup_object


def get_scene_details(background_name: str, pick_up_object_name: str):
    background = get_background(background_name)
    pick_up_object = get_pickup_object(pick_up_object_name)
    scene_details = {
        "background": background.get_background(),
        "pick_up_object": pick_up_object.get_pick_up_object(),
        "destination_object": background.get_destination(),
    }
    return scene_details
