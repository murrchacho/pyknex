from .base import Base

class Update(Base):
    def __init__(self, query):
        self.query = query
    
    def update(self, value):
        self.query += f'UPDATE {value} '

        return self