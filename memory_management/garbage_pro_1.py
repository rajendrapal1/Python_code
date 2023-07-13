import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True

    return False


obj1=ref_count('surat')
print(obj1)
obj2=object_exists(1)
print(obj2)