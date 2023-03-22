#!/usr/bin/env python3

# Import libraries
import os

# Declaration of functions
def generate_directory_info(path):
    for (root, dirs, files) in os.walk(path):
        # Print the current directory path
        print(f"Directory: {root}")
        
        # Print the sub-directories in the current directory
        print("Subdirectories: ")
        for dir in dirs:
            print(os.path.join(root, dir))
        
        # Print the files in the current directory
        print("Files: ")
        for file in files:
            print(os.path.join(root, file))
        
        print("\n")
        
        # Save output to a text file
        with open('directory_info.txt', 'a') as f:
            f.write(f"Directory: {root}\n")
            f.write("Subdirectories: \n")
            for dir in dirs:
                f.write(f"{os.path.join(root, dir)}\n")
            f.write("Files: \n")
            for file in files:
                f.write(f"{os.path.join(root, file)}\n")
            f.write("\n")
    
    # Open the output file with Libre Office Writer
    os.system('libreoffice --writer directory_info.txt')

def create_test_directory(path):
    dir_name = input("Enter directory name: ")
    test_dir_path = os.path.join(path, dir_name)
    if not os.path.exists(test_dir_path):
        os.makedirs(test_dir_path)
        os.makedirs(os.path.join(test_dir_path, "string_01"))
        os.makedirs(os.path.join(test_dir_path, "string_02"))
        os.makedirs(os.path.join(test_dir_path, "string_03"))
    return test_dir_path

# Main
if __name__ == '__main__':
    # Read user input for the directory path
    user_path = input("Enter a directory path: ")
    
    # Call the function to generate directory information
    generate_directory_info(user_path)
    
    # Call the function to create a test directory
    test_dir_path = create_test_directory("/home/roguione/Desktop")
    
    # Call the function again on the test directory
    generate_directory_info(test_dir_path)
    
# End
