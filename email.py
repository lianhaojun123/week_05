EMAIL_TO_NAME = {}


def main():
    email = input("Email: ")
    while email != "":
        name = email.split('@')[0]
        check_name = input("Is your name {} (Y/n)".format(name)).upper()
        if check_name != "" and check_name.upper() != "Y":
            name = input("Name:")
        EMAIL_TO_NAME[name] = email
        email = input("Email: ")
    for name, email in EMAIL_TO_NAME.items():
        print("{} ({})".format(name, email))
    print(EMAIL_TO_NAME)


main()
