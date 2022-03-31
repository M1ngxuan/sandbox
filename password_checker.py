"""
Description: A simple password checker
Name: Mingxuan Zhang
"""

MINIMUM_LENGTH = 8
def main():
    """start program"""
    password = input("Please enter a password at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < 8:
        print("Password is too short!")
        password = input("Pleas enter a password at least {} characters: ".format(MINIMUM_LENGTH))
    print("*" * len(password))
main()