import portfolio_management.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=portfolio_management.defs)
