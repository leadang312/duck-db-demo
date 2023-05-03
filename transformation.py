import duckdb

# Connect to the database
con = duckdb.connect('mydatabase.db')

# Creating new table
con.execute("CREATE TABLE newtable AS SELECT name FROM mytable")
