def user():
    userName = input("Enter your name: ")
    if len(userName) >= 3:
        print(" Hello " + userName + " How are you?")
    else:
        print("Minimum three character required")
    return


user()
