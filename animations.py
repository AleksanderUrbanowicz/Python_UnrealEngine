import unreal
import random


ACTORS_COUNT = (
    3,
    3,
    3
)

MESH_PATH = ''
ANIMATION_TIME = 10
CHANNELS_TO_KEY = [
    'Location.X',
    'Location.Y',
    'Location.Z'
]

log


def hello():
    unreal.log("hello animations script")


def main():
    unreal.log("main def")


def add_object_to_animation(target_animation, actor):
    fps = target_animation.get_display_rate()
    actor_location = actor.get_actor_location()
    actor_location_vector3 = [actor_location.x, actor_location.y, actor_location.z]
    animation = target_animation.add_possessable(actor)


def create_actor(location):
    cube=unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        location=location
    )
    mesh = unreal.load_object(None, MESH_PATH)