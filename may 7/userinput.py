# The user type something
user_input = input("Please type something: ")

#Save it to a file 'user_input.txt'
with open("user_input.txt", "w") as file:
    file.write(user_input)

# Read the content back from the file
with open("user_input.txt", "r") as file:
    content = file.read()

# Show what we read from the file
print("You typed: ", content)
