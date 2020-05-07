import unreal
from unreal import Vector

SEPARATION_VALUES = {
    'CUBE': 2000,
    'SPHERE': 5600,
    'OTHER': 9000,
    'WALL': -1000
}


def log_unreal():
    unreal.log("hello Unreal")


def separate_actors(label_prefix):
    level_actors = unreal.EditorLevelLibrary.get_all_level_actors()
    print('separate actors with prefix: '+label_prefix)
    for actor in level_actors:
        actor_label = actor.get_actor_label()
        if label_prefix in actor_label:
            print('placing: {}'.format(actor_label))
            actor_location = actor.get_actor_location()
            actor_bounds = actor.get_actor_bounds(False)
            actor_min_z = actor_bounds[0].z - actor_bounds[1].z
            location_offset = Vector(actor_location.x, actor_location.y, SEPARATION_VALUES['CUBE'])
            actor.set_actor_location(location_offset, False, False)

