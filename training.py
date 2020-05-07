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

SAVE_FILENAME = 'Save.txt'
SAVE_ABS_PATH = os.path.join(os.path.dirname(__file__), SAVE_FILENAME)

log_help()


def log(object):
    for n in object:
        unreal.log(n)


def save_actors_positions():
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir,  'Save.txt')
    backup = open(abs_file_path, "w+")
    backup.write(pickle.dumps(get_all_actors_positions()))
    backup.close()


def get_saved_positions():
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, 'Save.txt')
    backup = open(abs_file_path, "r")
    log(pickle.load(backup))


def get_all_actors():
    return unreal.EditorLevelLibrary.get_all_level_actors()


def get_all_actors_positions():
    actors_positions = {(n.get_actor_label(),
                         "%.2f" % n.get_actor_location().x,
                         "%.2f" % n.get_actor_location().y,
                         "%.2f" % n.get_actor_location().z) for n in get_all_actors()}
    log(actors_positions)
    return actors_positions


def get_all_actors_labels():
    level_actors = get_all_actors()
    level_actors_labels = [n.get_actor_label() for n in level_actors]
    return level_actors_labels


def get_actors_labels(prefix):
    labels_with_prefix = [n for n in get_all_actors_labels() if n.startswith(prefix)]
    for label in labels_with_prefix:
        unreal.log(label)


def log_all_actors_labels():
    for actor_label in get_all_actors_labels():
        unreal.log(actor_label)


def log_help():
    unreal.log(START_POSITIONS['Cube'].x)
    unreal.log(START_POSITIONS['Cube'].y)
    unreal.log(START_POSITIONS['Cube'].z)
    unreal.log(SAVE_ABS_PATH)

