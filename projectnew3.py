import tkinter as tk
from tkinter import messagebox
import random
import os

class NoAvailableSpaceException(Exception):
    pass

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
            raise NoAvailableSpaceException("No available spaces.")

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
        self.root.config(bg="Pink")  # Set background color for the root window

        self.parking_system = SmartParkingSystem(total_spaces)

        # Center frame with a border and background color
        self.center_frame = tk.Frame(root, bd=10, relief=tk.RIDGE, padx=10, pady=10, bg="Gray")
        self.center_frame.pack(padx=20, pady=20, expand=True)

        # Canvas to display parking diagram
        self.canvas = tk.Canvas(self.center_frame, width=400, height=200, bg="white")
        self.canvas.pack()

        # Load car image
        try:
            image_path = os.path.join(os.path.dirname(__file__), "car.png")
            self.car_image = tk.PhotoImage(file=r"C:\Users\Navya Sri\Downloads\car.png")
        except Exception as e:
            error_message = f"Error loading car image: {e}"
            print(error_message)
            messagebox.showerror("Image Load Error", error_message)
            self.car_image = None  # Fallback to no image

        # Labels for information display
        self.availability_label = tk.Label(self.center_frame, text="Available Spaces:", bg="lightgrey")
        self.availability_label.pack(pady=5)

        # Reserve button
        self.reserve_button = tk.Button(self.center_frame, text="Reserve Space", command=self.reserve_space)
        self.reserve_button.pack(pady=5)

        # Release button
        self.release_button = tk.Button(self.center_frame, text="Release Space", command=self.release_space)
        self.release_button.pack(pady=5)

        # Quit button
        self.quit_button = tk.Button(self.center_frame, text="Quit", command=root.destroy)
        self.quit_button.pack(pady=5)

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
            x = (space - 1) * 40
            y = 100
            if space in self.parking_system.reserved_spaces:
                if self.car_image:
                    self.canvas.create_image(x + 15, y + 15, image=self.car_image)
                else:
                    self.canvas.create_rectangle(x, y, x + 30, y + 30, fill="red")
            else:
                self.canvas.create_rectangle(x, y, x + 30, y + 30, fill="green")

    def reserve_space(self):
        try:
            reserved_space = self.parking_system.reserve_space()
            messagebox.showinfo("Reservation Successful", f"Space {reserved_space} reserved.")
        except NoAvailableSpaceException as e:
            messagebox.showerror("No Available Space", "No available spaces.")

    def release_space(self):
        if self.parking_system.reserved_spaces:
            space_to_release = random.choice(list(self.parking_system.reserved_spaces))
            if self.parking_system.release_space(space_to_release):
                messagebox.showinfo("Release Successful", f"Space {space_to_release} released.")
            else:
                messagebox.showerror("Error", f"Error releasing space {space_to_release}.")
        else:
            messagebox.showinfo("No Reserved Spaces", "There are no reserved spaces to release.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SmartParkingGUI(root, total_spaces=10)
    root.mainloop()

