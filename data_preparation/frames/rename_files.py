import os

folder = "c:/Users/alina/Master-Projects/applied-dl/data_preparation/frames/left_side_fullstroke/"
files = os.listdir(folder)

num = 0
for file in files:

    new_name = f"frame_{num:06d}.jpg"

    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"{old_path} renamed to {new_path}")
    
    num+=1