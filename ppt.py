import sqlite3

# Connect to a database (will create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER)''')

# Insert some data into the table
cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ('Bob', 25))

# Commit the changes
conn.commit()

# Close the cursor and connection when done
cursor.close()
conn.close()