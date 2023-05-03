import duckdb

# Connect to the database
con = duckdb.connect('mydatabase.db')

# Query the data from the table
result = con.execute("SELECT * FROM newtable")
for row in result.fetchall():
    print(row)