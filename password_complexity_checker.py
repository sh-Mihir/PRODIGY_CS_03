# Task 3


def passwordComplexityChecker(input_password):

    n = len(input_password)

    upperCaseCount = 0
    lowerCaseCount = 0
    digitCount = 0
    specialCharacters = "'-!\"#$%&()*,./:;?@[]^_`{|}~\+<=>"
    specialCharactersCount = 0
    normalCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    normalCharactersCount = 0
    sequentialCharacters = False
    repetitiveCharacters = False

    for i in range(n):
        if input_password[i] != " ":
            if input_password[i].isupper():
                upperCaseCount += 1
            if input_password[i].islower():
                lowerCaseCount += 1
            if input_password[i].isdigit():
                digitCount += 1
            if input_password[i] in specialCharacters:
                specialCharactersCount += 1
            if input_password[i] in normalCharacters:
                normalCharactersCount += 1
            for i in range(n - 1):
                if input_password[i] == input_password[i + 1]:
                    repetitiveCharacters = True
                if ord(input_password[i]) + 1 == ord(input_password[i + 1]):
                    sequentialCharacters = True
                if ord(input_password[i]) == ord(input_password[i + 1]) + 1:
                    sequentialCharacters = True
        else:
            print("Do not use space in between characters")
            return

    if (
        upperCaseCount > 0
        and lowerCaseCount > 0
        and digitCount > 0
        and specialCharactersCount > 0
        and normalCharactersCount > 0
        and not sequentialCharacters
        and not repetitiveCharacters
        and 8 <= n <= 64
    ):
        print()
        print(f"Password contains {upperCaseCount} uppercase letter.")
        print(f"Password contains {lowerCaseCount} lowercase letter.")
        print(f"Password contains {digitCount} digits.")
        print(f"Password contains {specialCharactersCount} special characters.")
        print(
            f"Password doesn't contain any sequential and repetitive characters in it."
        )
        print(f"Password length: {n} characters.")
        print()
        print("Password is strong.")

    elif (
        upperCaseCount > 0
        and lowerCaseCount > 0
        and digitCount > 0
        and specialCharactersCount > 0
        and normalCharactersCount > 0
        and 5 <= n < 8
    ):
        print()
        print(f"Password contains {upperCaseCount} uppercase letter.")
        print(f"Password contains {lowerCaseCount} lowercase letter.")
        print(f"Password contains {digitCount} digits.")
        print(f"Password contains {specialCharactersCount} special characters.")
        print(
            f"Password may or may not contain sequential or repetitive characters in it."
        )
        print(f"Password length: {n} characters.")
        print()
        print("Password is moderate.")
        print()
        print("Suggestion:-\n")
        print("You should avoid using sequential or repetition of characters.")
        print("Your password must have at least 8 or more characters.")
        print()

    else:
        print()
        print(f"Password contains {upperCaseCount} uppercase letter.")
        print(f"Password contains {lowerCaseCount} lowercase letter.")
        print(f"Password contains {digitCount} digits.")
        print(f"Password contains {specialCharactersCount} special characters.")
        print(
            f"Password may or may not contain sequential or repetitive characters in it."
        )
        print(f"Password length: {n} characters.")
        print()
        print("Password is weak.")
        print()
        print("Suggestion:-\n")
        print(
            "Your password must contain atleast one uppercase, one lowercase, one digit and one special character."
        )
        print("You should avoid using sequential or repetition of characters.")
        print("Your password must have at least 8 or more characters.")
        print()


if __name__ == "__main__":
    print()
    print(
        "--------------------Welcome to Password Complexity Checker Tool--------------------"
    )
    print()

    print("Enter your password here: ")
    input_password = input()

    passwordComplexityChecker(input_password)
