"""Module providing a Select class for pyknex."""
from typing import Self
from . base import Base

class Select(Base):
    """Class providing a Select operator for pyknex."""
    def select(self, value: str) -> Self:
        """Method providing a Select operator functionality for pyknex."""
        self.query += f'SELECT {value} FROM {self.meta.table_name}'

        return self
