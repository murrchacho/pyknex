"""Module providing a Pyknex class for pyknex."""
from . classes import Meta, Select, Update

class Pyknex(Select, Update):
    """Class providing an Pyknex class that is used to initialize pyknex."""
    def __init__(self, table_name, **kwargs):
        meta = Meta(table_name, **kwargs)
        super().__init__(meta)
