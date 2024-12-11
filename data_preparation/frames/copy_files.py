import os
import shutil

def copy_every_5th_file(source_folder, destination_folder):

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = sorted(os.listdir(source_folder))  # Sorting to maintain order
    
    # Copy every 5th file
    for i in range(0, len(files), 5): 
        file_path = os.path.join(source_folder, files[i])
        destination_path = os.path.join(destination_folder, files[i])
        
        shutil.copy2(file_path, destination_path)
        print(f'Copied "{files[i]}" to "{destination_folder}"')

copy_every_5th_file("c:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data_preparation/frames/left_side_fullstroke", 
                    "c:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data_preparation/temp")