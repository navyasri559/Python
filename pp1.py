import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to select all rows from my_table
cursor.execute("SELECT * FROM my_table")

# Fetch all rows
rows = cursor.fetchall()

# Print the retrieved rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn .close()
