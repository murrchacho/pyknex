"""Module providing an Update class for pyknex."""
from typing import Self
from . base import Base

class Update(Base):
    """Class providing an Update operator for pyknex."""
    def update(self, value) -> Self:
        """Method providing an Update operator functionality for pyknex."""
        self.query += f'UPDATE {value} '

        return self
