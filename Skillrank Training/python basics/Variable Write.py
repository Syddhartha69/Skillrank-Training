# this is my third code in python
# the following code is used for storing value of the entered variable in another file


text = "This is my text to be stord in another file" # the value which is supposed to be stored in the text file is entered here
file_name = "Variable Stored.txt" # this is the destination file - if there is a file that already exists, it stores there, but if no file exist with such name, it creates one

with open(file_name,'w') as file: # opening the text file to write the given input value  
    file.write(text)

print(f"Value Saved to {file_name}") # this line is used to make sure that the code has run correctly and displays message in the terminal 