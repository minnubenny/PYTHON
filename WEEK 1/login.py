# Simple user credentials
username = "admin"
password = "1234"

# Get input from user
user = input("Username: ")
pwd = input("Password: ")

# Check credentials
if user == username and pwd == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
