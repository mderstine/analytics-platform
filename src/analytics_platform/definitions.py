import analytics_platform.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=analytics_platform.defs)
