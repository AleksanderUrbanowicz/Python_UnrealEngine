import unreal
import os
import cPickle as pickle
from unreal import Vector

START_POSITIONS = {
    'Cube': Vector(1, 2, 3),
    'Sphere': Vector(5, 5, 5),
    'Wall': Vector(20, 20, 20)
}

DIRECTIONS_AND_GAP = {
    'Cube': Vector(100, 0, 0),
    'Sphere': Vector(0, 500, 0),
    'Wall': Vector(0, 0, 200)
}

LOG = False
SAVE_FILENAME = 'Save.txt'
SAVE_ABS_PATH = os.path.join(os.path.dirname(__file__), SAVE_FILENAME)

log_start()
save_actors_positions()


# # # # # IO # # # # #


def save_actors_positions():
    backup = open(SAVE_ABS_PATH, "w+")
    backup.write(pickle.dumps(get_all_actors_positions()))
    backup.close()


def get_saved_positions():
    backup = open(SAVE_ABS_PATH, "r")
    saved_positions = pickle.load(backup)
    if LOG:
        log(saved_positions)
    backup.close()
    return saved_positions


# # # # # Actors # # # # #
# Getters #
def get_all_actors():
    return unreal.EditorLevelLibrary.get_all_level_actors()


def get_all_actors_labels():
    level_actors = get_all_actors()
    level_actors_labels = [n.get_actor_label() for n in level_actors]
    return level_actors_labels


def get_actors_labels(prefix):
    labels_with_prefix = [n for n in get_all_actors_labels() if n.startswith(prefix)]
    if LOG:
        log(labels_with_prefix)
    return labels_with_prefix


def get_all_actors_positions():
    actors_positions = {(n.get_actor_label(),
                         "%.2f" % n.get_actor_location().x,
                         "%.2f" % n.get_actor_location().y,
                         "%.2f" % n.get_actor_location().z) for n in get_all_actors()}
    if LOG:
        log(actors_positions)
    return actors_positions


# Setters #
def load_positions_from_backup():
    print('load_positions_from_backup')
    actors = get_all_actors()
    saved_positions = get_saved_positions()
    unreal.log(type(actors))
    unreal.log(type(saved_positions))
    for actor in actors:
        actor.set_actor_location(saved_positions[""], False, False)


def set_positions():
    print('set_positions')


# # # # # Logs # # # # #


def log_start():
    unreal.log(START_POSITIONS['Cube'].x)
    unreal.log(START_POSITIONS['Cube'].y)
    unreal.log(START_POSITIONS['Cube'].z)
    unreal.log(SAVE_ABS_PATH)


def log(object):
    for n in object:
        unreal.log(n)

