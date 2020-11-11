"""
author -Maruti Bhosale
date -11-11-2020
time -15:20
package -basic_core_programs
Statement -printing user name with message

"""


def user():
    userName = input("Enter your name: ")
    if len(userName) >= 3:
        print(" Hello " + userName + " How are you?")
    else:
        print("Minimum three character required")
    return


if __name__ == "__main__":
    user()
