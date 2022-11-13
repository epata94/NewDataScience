import sys

def greet_users(usernames):
    # a = usernames[:1].upper()
    # b = usernames[1:]
    # usernames = a + b
    usernames = usernames[0].upper() + usernames[1:]
    return usernames

usernames = sys.argv[1:]
for users in usernames:
    users = greet_users(str(users))
    print("Hello, %s!" % users)

