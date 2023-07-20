import oomp

import oomp_kicad


oomp.load_parts()
oomp.create_parts_readme()

oomp_kicad.create_footprint_library()
oomp_kicad.create_symbol_library()