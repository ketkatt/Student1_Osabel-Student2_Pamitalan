# Exercise 2: File Handling

# 1. Create a Python program that:
# a. Ask user to enter a short note/message
note = input("Enter a short note/message: ")

# b. Save the message into a file named notes.txt (use “w” mode)
with open("notes.txt", "w") as file:
    file.write(note + "\n")

print("\nYour note has been saved to notes.txt.\n")

# 2. Read File:
try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print("Current contents of notes.txt:\n")
        print(content)
except FileNotFoundError:
    print("Error: The file notes.txt was not found!")

# 3. Append new data:
new_note = input("\nEnter another note/message to add: ")

with open("notes.txt", "a") as file:
    file.write(new_note + "\n")

# Display the updated content
try:
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print("\nUpdated contents of notes.txt:\n")
        print(updated_content)
except FileNotFoundError:
    print("Error: Unable to read notes.txt after append.")
