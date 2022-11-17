str = 'janny hannah margot kevin min'

usernames = str.split()
def greet_users(usernames) :
    for name in usernames :
        print(f'Hello, {name.capitalize()}')

greet_users(usernames)