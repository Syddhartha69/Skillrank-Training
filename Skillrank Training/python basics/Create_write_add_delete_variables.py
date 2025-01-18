# this is my fourth code in python
# the following code is used for writing text in another file, rewriting text in new line, and deleting the file 


# for inserting first value
text = "This is my text to be stored in another file" # the value which is supposed to be stored in the text file is entered here
file_name = "Variable Store, Add and Delete.txt" # this is the destination file - if there is a file that already exists, it stores there, but if no file exist with such name, it creates one

with open(file_name,'w') as file: # opening the text file to write the given input value  # 'w' means to write in the file
    file.write(text)

print(f"First Value Saved to {file_name}") # this line is used to make sure that the code has run correctly and displays message in the terminal 



# this is for inserting new line 
new_line = "This is my new line in the file" # this is the new line to be written in text file 
file_name = "Variable Store, Add and Delete.txt" # this is the destination file 

with open(file_name,'a') as file: # opening the text file to write the given input value   # 'a' means to append in the file
    file.write("\n" + new_line)

print(f"New Value Saved to {file_name}") # this line is used to make sure that the code has run correctly and displays message in the terminal 



# return the value from the file
with open(file_name, 'r') as file:
    content = file.read()

print("File content:")
print(content)



# this is for deleting the contents in the file by overwriting with empty string
if content:
    with open(file_name, "w") as file:
        pass  # This truncates the file to 0 bytes
    print(f"File {file_name} cleared (simulated deletion).") # this message is displayed if there is something written in the file and has been cleared  
else:
    print(f"File {file_name} was not cleared.") # this message is displayed if there is nothing written in the file and has been cleared 

