from pyknex import Pyknex as pk

result = (pk("table_name")
 .select("*")
 .log()
)