import os

def get_file_size(file_path):
    return os.path.getsize(file_path) * 8 / (1024 * 1024)

def get_files_in_directory(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def get_file_sizes(directory):
    file_sizes = {}
    files = get_files_in_directory(directory)

    for file in files:
        file_path = os.path.join(directory, file)
        size_in_megabits = get_file_size(file_path)
        file_sizes[file] = size_in_megabits

    return file_sizes

# Specify the directory paths for different datasets
cityscapes_directory = "./cityscapes_100_images/"
coco_directory = "./coco_100_images/"
imagenet_directory = "./imagenet_100_images/"

# Function to print max and min file sizes for a given directory
def print_max_min_sizes(directory_path):
    file_sizes = get_file_sizes(directory_path)
    
    # Find the max and min file sizes
    max_file = max(file_sizes, key=file_sizes.get)
    min_file = min(file_sizes, key=file_sizes.get)

    # Print the max and min file sizes
    print("Dataset: {}".format(os.path.basename(os.path.normpath(directory_path))))
    print("Maximum file size:")
    print("{}: {:.2f} Mb".format(max_file, file_sizes[max_file]))

    print("\nMinimum file size:")
    print("{}: {:.2f} Mb".format(min_file, file_sizes[min_file]))
    print("\n")

# Print max and min file sizes for each dataset
print_max_min_sizes(cityscapes_directory)
print_max_min_sizes(coco_directory)
print_max_min_sizes(imagenet_directory)
