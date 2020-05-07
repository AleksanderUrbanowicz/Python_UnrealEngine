import unreal
from unreal import Vector

lst_actors = unreal.EditorLevelLibrary.get_all_level_actors()
print('place actors at 0 z')
for act in lst_actors:
    act_label = act.get_actor_label()
    if 'Cube' in act_label:
        print('placing: {}'.format(act_label))
        act_location = act.get_actor_location()
        act_bounds = act.get_actor_bounds(False)
        act_min_z = act_bounds[0].z - act_bounds[1].z
        location_offset = Vector(act_location.x, act_location.y, act_location.z - act_min_z)
        act.set_actor_location(location_offset, False, False)