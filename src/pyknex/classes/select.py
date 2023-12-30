"""Module providing a Select class for SQL builder."""
from typing import Self
from . base import Base

class Select(Base):
    """Class providing a Select operator for SQL builder."""
    def select(self, value: str) -> Self:
        """Method providing a Select operator functionality for SQL builder."""
        self.query += f'SELECT {value} '

        return self
