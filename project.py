#smart parking system
import tkinter as tk
import random


class SmartParkingSystem:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces
        self.reserved_spaces = set()

    def check_availability(self):
        return self.available_spaces

    def reserve_space(self):
        if self.available_spaces > 0:
            space_number = random.randint(1, self.total_spaces)
            while space_number in self.reserved_spaces:
                space_number = random.randint(1, self.total_spaces)

            self.reserved_spaces.add(space_number)
            self.available_spaces -= 1
            return space_number
        else:
            return None

    def release_space(self, space_number):
        if space_number in self.reserved_spaces:
            self.reserved_spaces.remove(space_number)
            self.available_spaces += 1
            return True
        else:
            return False


class SmartParkingGUI:
    def __init__(self, root, total_spaces):
        self.root = root
        self.root.title("Smart Parking System")

        self.parking_system = SmartParkingSystem(total_spaces)

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

    def reserve_space(self):
        reserved_space = self.parking_system.reserve_space()
        if reserved_space is not None:
            print(f"Space {reserved_space} reserved.")
        else:
            print("No available spaces.")

    def release_space(self):
        space_to_release = random.choice(list(self.parking_system.reserved_spaces))
        if self.parking_system.release_space(space_to_release):
            print(f"Space {space_to_release} released.")
        else:
            print(f"Error releasing space {space_to_release}.")


if __name__ == "__main__":
    root = tk.Tk()
    gui = SmartParkingGUI(root, total_spaces=10)
    root.mainloop()