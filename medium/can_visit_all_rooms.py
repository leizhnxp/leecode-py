from typing import List, Set


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    if 0 < len(rooms) < 2:
        return True
    room_keys = rooms[0]
    if len(room_keys) == 0:
        return False
    collected_keys = set([x for x in filter(lambda x: x < len(rooms), room_keys)])

    collected_keys.add(0)

    while True:
        new_keys = extend_keys(collected_keys, rooms)
        if len(new_keys) > len(collected_keys):
            collected_keys = new_keys
            continue
        else:
            if len(new_keys) == len(rooms):
                return True
            else:
                return False


def extend_keys(collected_keys: Set[int], rooms: List[List[int]]) -> Set[int]:
    collected_keys_tmp = set()
    for key in collected_keys:
        new_keys = rooms[key]
        for new_key in new_keys:
            if new_key not in collected_keys_tmp:
                collected_keys_tmp.add(new_key)
            else:
                pass
    return collected_keys.union(collected_keys_tmp)


def has_new_key(keys_in_room: List[int], not_found_keys: List[int]):
    pass
