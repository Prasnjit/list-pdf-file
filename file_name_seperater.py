import os

# Directory path where the files are located
directory = '.'

# Array to store the separated file names
file_names = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # if we change .isdif to .isfile then it will scan all the file
    if os.path.isdir(os.path.join(directory, filename)):
        # Split the file name using "_"
        separated_names = filename.split("_")
        file_names.extend(separated_names)

# Print the separated file names
print(file_names)



# this program is to saperate the directory name havinge "_" and store the name in array 
# it can be use to identify the request from different input