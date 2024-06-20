import os

def find_file(file_name, directory="."):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Found '{file_name}' at: {file_path}")
            return file_path  # Return the file path if found
    print(f"'{file_name}' not found in {directory}")
    return None  # Return None if file not found

if __name__ == "__main__":
    file_name = "car.png"
    file_path = find_file(file_name)
    if file_path:
        print("File path:", file_path)
