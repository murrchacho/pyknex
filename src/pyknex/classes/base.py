"""Module providing a base class for all pyknex classes."""
from . meta import Meta

class Base:
    """Class providing a common methods for all pyknex classes."""
    def __init__(self, meta: Meta):
        self.query = ""
        self.meta = meta

    def log(self) -> str:
        """Prints out a SQL query that is being processed at this operator"""
        print(self.query)
