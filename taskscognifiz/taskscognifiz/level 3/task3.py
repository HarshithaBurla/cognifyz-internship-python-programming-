import os
import shutil

def organize_files(directory):
    # Define the types of files to organize
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav']
    }

    # Create folders for file types if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Scan files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Identify file type and move
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Create new name with numbering
                new_filename = f"{folder}_{len(os.listdir(os.path.join(directory, folder))) + 1}{file_extension}"
                shutil.move(file_path, os.path.join(directory, folder, new_filename))
                print(f"Moved {filename} to {folder}/{new_filename}")
                moved = True
                break
        
        # Handle unknown file types
        if not moved:
            unknown_folder = os.path.join(directory, 'Others')
            if not os.path.exists(unknown_folder):
                os.makedirs(unknown_folder)
            shutil.move(file_path, os.path.join(unknown_folder, filename))
            print(f"Moved {filename} to Others/")
    
    print("Files organized successfully!")

# Usage
directory_path = input("Enter the directory path: ")
organize_files(directory_path)
#output
##= RESTART: C:\taskscognifiz\level 3\task3.py
##Enter the directory path: C:\Users\harik\OneDrive\Desktop\Documents\dataauto
##Files organized successfully!
