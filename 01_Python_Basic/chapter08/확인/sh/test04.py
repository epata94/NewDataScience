import sys

def greet_users(usernames):
    for argument in usernames[1:]:
        print(f'Hello, {argument.capitalize()}!')

usernames = sys.argv[:]

greet_users(usernames)
