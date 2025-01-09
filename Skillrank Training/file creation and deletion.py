# this is my fifth code in python 
# this code is used to create a file, copy its content and paste it in another file and lastly delete the firstly created file  


import os  # To handle file deletion os is imported

# File names for the file creation
file1 = "file1.txt"
file2 = "file2.txt"

# Step 1: Create and write content to file1
with open(file1, "w") as fl1:
    fl1.write("This is the value inserted in file1.\nThis values will be copied from file1 and paste to file2.")

print(f"Value inserted in {file1}.")


# Step 2: Read content from file1
with open(file1, "r") as fl1:
    content = fl1.read()

print(f"Value read from {file1}.")


# Step 3: Write content from file1 to file2
with open(file2, "w") as fl2:
    fl2.write(content)

print(f"Value inserted to {file2}.")


# Step 4: Delete file1
if os.path.exists(file1):
    os.remove(file1)
    print(f"{file1} has been deleted.")
else:
    print(f"{file1} does not exist.")

