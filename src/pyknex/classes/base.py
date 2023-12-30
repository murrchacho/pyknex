"""Module providing a base class for all pyknex classes."""
class Base:
    """Class providing a common methods for all pyknex classes."""
    def __init__(self):
        self.query = ""

    def log(self) -> str:
        """Prints out a SQL query that is being processed at this operator"""
        print(self.query)
