from .base import Base

class Select(Base):
    def __init__(self, query):
        self.query = query
    
    def select(self, value):
        self.query += f'SELECT {value} '

        return self