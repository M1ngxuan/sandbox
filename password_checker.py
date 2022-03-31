MINIMUM_LENGTH = 8
def main():
    password = input("Please enter a password at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < 8:
        print("Password is too short!")
        password = input("Pleas enter a password at least {} characters: ".format(MINIMUM_LENGTH))
    print("*" * len(password))
main()