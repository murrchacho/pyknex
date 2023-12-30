from pyknex import Pyknex as pk

result = (pk("qwd")
 .select("*")
 .log()
)