"""
Module 2 — Activity: File Sorting with os and shutil
Student: Alex Rivera
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a Python script that automatically scans an unsorted directory 
(such as a "Downloads" or "Desktop" folder) and organizes all the files 
into categorized subfolders based on their file extensions (e.g., .png, 
.pdf, .xlsx). 

The sorting rule works by:
1. Inspecting each file's extension in the target folder.
2. Checking a pre-defined map of categories (Images, Documents, Spreadsheets, Code, Archives).
3. Automatically creating any missing destination folder using os.makedirs().
4. Moving the file to its corresponding folder using shutil.move().
Files with unknown extensions are safely moved to an "Others" directory.


============================================
KEY VOCABULARY
============================================
- os module: A built-in Python library that lets your script interact with the 
  operating system to perform tasks like inspecting folder contents, checking if 
  paths exist, and making new directories.
- shutil module: A higher-level Python library designed for utility file operations, 
  such as copying, moving, renaming, or deleting entire files and folder trees.
- file path: The unique address/string that pinpoints exact file or folder locations 
  within a file system (e.g., "C:/Users/Alex/Downloads/report.pdf").
- directory: Another name for a folder on a computer system used to store and group files.
- extension: The suffix at the end of a filename following a period (e.g., .txt, .png) 
  that tells the operating system what type of file it is.


============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

def organize_folder(target_directory):
    # Mapping of target folder names to their corresponding file extensions
    EXTENSION_MAP = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf"],
        "Spreadsheets": [".xlsx", ".xls", ".csv"],
        "Code": [".py", ".js", ".html", ".css", ".json"],
        "Archives": [".zip", ".tar", ".gz", ".7z"]
    }

    # Ensure target directory exists before running
    if not os.path.exists(target_directory):
        print(f"Error: Directory '{target_directory}' does not exist.")
        return

    # Iterate over all items in the target directory
    for item in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item)

        # Skip directories to avoid moving folders into themselves
        if os.path.isdir(item_path):
            continue

        # Extract file extension (converted to lowercase for consistency)
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Determine which destination folder the file belongs to
        destination_folder = "Others"
        for folder_name, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                destination_folder = folder_name
                break

        # Create the subfolder path and make the folder if it doesn't exist
        dest_dir_path = os.path.join(target_directory, destination_folder)
        os.makedirs(dest_dir_path, exist_ok=True)

        # Move the file to the destination directory
        destination_file_path = os.path.join(dest_dir_path, item)
        
        # Handle potential filename collisions before moving
        if not os.path.exists(destination_file_path):
            shutil.move(item_path, destination_file_path)
            print(f"Moved: '{item}' -> '{destination_folder}/'")
        else:
            print(f"Skipped: '{item}' already exists in '{destination_folder}/'")

if __name__ == "__main__":
    # Replace this path with the path to your target folder
    target_folder = "./test_folder" 
    organize_folder(target_folder)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
When I first ran my script, I forgot to add `if os.path.isdir(item_path): continue`. 
Because of this, when the script created the "Images" folder on the first loop, 
it then tried to treat the newly created "Images" directory as a file during subsequent 
loops! This resulted in a `PermissionError` when `shutil.move` tried to process a folder 
instead of a normal file. Checking `os.path.isdir()` resolved the problem immediately.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This script directly mirrors how administrative workflows and gradebook systems handle 
files. For instance, teachers and school administrators often receive hundreds of digital 
assignments, attendance rosters, and student exports named inconsistently in a single 
download folder. 

Using `os` and `shutil`, an automated script can scan a submission directory, extract 
student IDs or assignment names from file titles, create individual student folders, and 
organize submissions instantly—saving hours of manual sorting every term.
"""