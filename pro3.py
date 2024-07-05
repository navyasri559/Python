import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector
from mysql.connector import Error

class NoAvailableSpaceException(Exception):
    pass

class SmartParkingSystem:
    def __init__(self, total_spaces, db_config):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces
        self.reserved_spaces = set()

        # Connect to MySQL database
        self.connection = self.connect_to_db(db_config)
        if self.connection:
            self.cursor = self.connection.cursor()
            # Initialize the database table
            self.setup_db()
            self.update_local_state()
        else:
            self.cursor = None

    def connect_to_db(self, db_config):
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                print("Connected to MySQL database")
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def setup_db(self):
        if self.cursor:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS parking_spaces (
                    space_number INT PRIMARY KEY,
                    reserved BOOLEAN NOT NULL
                )
            ''')
            self.connection.commit()

            # Initialize parking spaces if the table is empty
            self.cursor.execute('SELECT COUNT(*) FROM parking_spaces')
            if self.cursor.fetchone()[0] == 0:
                for space_number in range(1, self.total_spaces + 1):
                    self.cursor.execute('INSERT INTO parking_spaces (space_number, reserved) VALUES (%s, %s)', (space_number, False))
                self.connection.commit()

    def update_local_state(self):
        if self.cursor:
            self.cursor.execute('SELECT space_number FROM parking_spaces WHERE reserved = TRUE')
            self.reserved_spaces = {row[0] for row in self.cursor.fetchall()}
            self.available_spaces = self.total_spaces - len(self.reserved_spaces)
            print(f"Updated local state: reserved_spaces={self.reserved_spaces}, available_spaces={self.available_spaces}")

    def check_availability(self):
        return self.available_spaces

    def reserve_space(self):
        if self.available_spaces > 0:
            space_number = random.randint(1, self.total_spaces)
            while space_number in self.reserved_spaces:
                space_number = random.randint(1, self.total_spaces)

            self.cursor.execute('UPDATE parking_spaces SET reserved = TRUE WHERE space_number = %s', (space_number,))
            self.connection.commit()

            self.reserved_spaces.add(space_number)
            self.available_spaces -= 1
            print(f"Reserved space {space_number}")
            return space_number
        else:
            raise NoAvailableSpaceException("No available spaces.")

    def release_space(self, space_number):
        if space_number in self.reserved_spaces:
            self.cursor.execute('UPDATE parking_spaces SET reserved = FALSE WHERE space_number = %s', (space_number,))
            self.connection.commit()

            self.reserved_spaces.remove(space_number)
            self.available_spaces += 1
            print(f"Released space {space_number}")
            return True
        else:
            return False

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

class SmartParkingGUI:
    def __init__(self, root, total_spaces, db_config):
        self.root = root
        self.root.title("Smart Parking System")

        self.parking_system = SmartParkingSystem(total_spaces, db_config)

        # Canvas to display parking diagram
        self.canvas = tk.Canvas(root, width=400, height=200, bg="white")
        self.canvas.pack()

        # Labels for information display
        self.availability_label = tk.Label(root, text="Available Spaces:")
        self.availability_label.pack()

        # Reserve button
        self.reserve_button = tk.Button(root, text="Reserve Space", command=self.reserve_space)
        self.reserve_button.pack()

        # Release button
        self.release_button = tk.Button(root, text="Release Space", command=self.release_space)
        self.release_button.pack()

        # Quit button
        self.quit_button = tk.Button(root, text="Quit", command=root.destroy)
        self.quit_button.pack()

        # Update GUI
        self.update_gui()

    def update_gui(self):
        # Update availability label
        self.availability_label.config(text=f"Available Spaces: {self.parking_system.check_availability()}")

        # Draw parking diagram
        self.draw_parking_diagram()

        # Schedule the update every 2000 milliseconds (2 seconds)
        self.root.after(2000, self.update_gui)

    def draw_parking_diagram(self):
        self.canvas.delete("all")
        total_spaces = self.parking_system.total_spaces
        for space in range(1, total_spaces + 1):
            color = "green" if space not in self.parking_system.reserved_spaces else "red"
            x = (space - 1) * 40
            y = 100
            self.canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
        print(f"Drew parking diagram with reserved spaces: {self.parking_system.reserved_spaces}")

    def reserve_space(self):
        try:
            reserved_space = self.parking_system.reserve_space()
            print(f"Space {reserved_space} reserved.")
        except NoAvailableSpaceException as e:
            print(e)
            messagebox.showerror("No Available Space", "No available spaces.")

    def release_space(self):
        if self.parking_system.reserved_spaces:
            space_to_release = random.choice(list(self.parking_system.reserved_spaces))
            if self.parking_system.release_space(space_to_release):
                print(f"Space {space_to_release} released.")
            else:
                print(f"Error releasing space {space_to_release}.")
        else:
            messagebox.showerror("No Reserved Space", "No reserved spaces to release.")

if __name__ == "__main__":
    db_config = {
        'user': 'root',
        'password': 'Navyasri@1234',
        'host': 'localhost',
        'database': 'smp'
    }

    root = tk.Tk()
    gui = SmartParkingGUI(root, total_spaces=10, db_config=db_config)
    root.mainloop()
