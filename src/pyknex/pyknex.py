from pyknex.classes.select import Select
from pyknex.classes.update import Update

class pyknex(Select, Update):
    def __init__(self, query=""):
        super().__init__(query)