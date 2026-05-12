import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def get_age():
    while True:
        try:
            return int(input("Enter an age to filter users: "))
        except ValueError:
            continue


def get_email():
    while True:
        email = input("Enter an email to filter users: ")
        if '@' in email:
            if '.' in email:
                return email
        print("Invalid email. Please try again.")


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? ('name', 'age', 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = get_age()
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = get_email()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
