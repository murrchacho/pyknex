"""Module providing an Update class for SQL builder."""
from typing import Self
from . base import Base

class Update(Base):
    """Class providing an Update operator for SQL builder."""
    def update(self, value) -> Self:
        """Method providing an Update operator functionality for SQL builder."""
        self.query += f'UPDATE {value} '

        return self
