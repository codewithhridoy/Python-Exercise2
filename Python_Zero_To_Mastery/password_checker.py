username = input("Enter Your Username: \n")
password = input("Enter Your Password: \n")

password_length = len(password)
hidden_password = password_length * '*'

print(f"Hello, {username} your Password {hidden_password} is {password_length} characters long")
