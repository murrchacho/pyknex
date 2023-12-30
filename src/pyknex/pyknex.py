"""Module providing a Pyknex class for SQL builder."""
from . classes import Select, Update

class Pyknex(Select, Update):
    """Class providing an Pyknex class that is used to initialize SQL builder."""
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name

    @property
    def table_name(self) -> str:
        """Returns a table name that is used by a query to perform."""
        return self.table_name

    @table_name.setter 
    def table_name(self, value):
        if (not isinstance(value, str) or len(value) == 0):
            raise ValueError("Name of table can't be an empty string!")

        self._table_name = value
