
import importlib

part_types = []
part_types.append("led")
part_types.append("ic")
part_types.append("mounting_hole")
part_types.append("header")

for type in part_types:
    importlib.import_module(f'oomp_create_parts_{type}')

def load_parts(**kwargs):
    print("loading parts started")
    for type in part_types:
        importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)