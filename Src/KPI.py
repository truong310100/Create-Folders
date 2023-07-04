from tkinter import *
from tkinter import messagebox
import os

def create_folders():
    # Create output folder if not exists
    output_folder = "FolderExport"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Create each folder
    for folder_name in input_text.get("1.0", END).strip().split("\n"):
        # Replace special characters with underscore
        folder_name = folder_name.replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")
        folder_path = os.path.join(output_folder, folder_name)
        os.mkdir(folder_path)
            
    # Show success message
    messagebox.showinfo("Success", "Folders created successfully.")



# Create UI components
root = Tk()
root.title('Create KPI')
input_text = Text(root, width=100, height=10, wrap="word")
input_text.pack()
btn_ok = Button(root, text="OK", width=10, command=create_folders)
btn_ok.pack(side=RIGHT, padx=10)
root.mainloop()