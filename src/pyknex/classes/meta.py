"""Module providing a Meta class for pyknex."""

class Meta():
    """Class providing a Metadata (connection information) information for all pyknex classes."""
    def __init__(self, table_name, **kwargs):
        self.table_name = table_name
        self.connection_params = kwargs

    @property
    def table_name(self) -> str:
        """Returns a table name that is used by a query to perform."""
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        if (not isinstance(value, str) or len(value) == 0):
            raise ValueError("Name of table can't be an empty string!")

        self._table_name = value
