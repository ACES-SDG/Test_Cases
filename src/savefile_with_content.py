import tkinter as tk
from tkinter import filedialog
import os 
def save_file():
    # Get the user's home directory (usually the "Documents" folder)
    home_directory = os.path.expanduser("/")
    print(home_directory)
    # Specify the folder name you want to create
    aces_folder = "ACES Analytics"

    # Create the full path for the folder
    aces_folder_path = os.path.join(home_directory, aces_folder)
    print(aces_folder_path)
    # Create the folder if it doesn't exist
    if not os.path.exists(aces_folder_path):
        os.makedirs(aces_folder_path)

    # Set the initial directory as the created folder
    initial_directory = aces_folder_path

    # Specify the filename
    file_name = "sample.txt"

    # Set the full path for the file
    file_path = os.path.join(initial_directory, file_name)
    
    files = [('ACES Analytics tool', '*.owbx')]
    
    file_path = filedialog.asksaveasfilename(initialfile= 'My work',initialdir=initial_directory, filetypes = files, defaultextension = files,)
    if file_path:
        with open(file_path, "w") as file:
            file.write("This is some sample text that you can save to a file.")

root = tk.Tk()
root.title("Save File Example")

save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(pady=20)

root.mainloop()
