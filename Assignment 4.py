with open("myblog.txt", "r") as file:
    content = file.read()

# Modified file
modified_content = content.upper()

with open("myblog.txt", "w") as file:
    file.write(modified_content)
print(content)

# This program asks the user for a filename and handles errors

filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        file = file.read()
        print(f"File content: {file}")
except FileNotFoundError:
    print("File not found, Please check again")

