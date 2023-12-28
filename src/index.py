from pyknex.pyknex import pyknex

pk = pyknex()

result = (pk
 .select("*")
 .update("+")
 .log()
)