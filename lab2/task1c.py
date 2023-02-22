def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    password = password.lower()
    if (password == "abc$123"):
        print("Welcome!")
    else:
        print("I don't know you.")

login() 