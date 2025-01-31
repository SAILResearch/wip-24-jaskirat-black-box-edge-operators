import os
import shutil
import re

def organize_txt_files():
    # Get the current directory
    current_dir = os.getcwd()

    # List all .txt files in the current directory
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]


    for txt_file in txt_files:
        # Extract the folder name from the file name before '_results'
        if '_results' in txt_file:
            # Split at '_results' and remove unwanted parts like "50mbps"
            folder_name = txt_file.split('_results')[0]
            # Remove bandwidth-related substrings (e.g., "50mbps", "100mbps")
            folder_name = re.sub(r'\d+mbps', '', folder_name).strip('_')
            
            # Create the folder if it doesn't exist
            folder_path = os.path.join(current_dir, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the txt file to the corresponding folder
            src_path = os.path.join(current_dir, txt_file)
            dest_path = os.path.join(folder_path, txt_file)
            shutil.move(src_path, dest_path)

            print(f"Moved {txt_file} to {folder_path}")

if __name__ == "__main__":
    organize_txt_files()
