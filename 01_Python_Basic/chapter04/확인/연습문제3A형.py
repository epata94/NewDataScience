message = ('spam','ham','spam','ham','spam')

list = []

for i in message :
    if i == 'spam' :
        x = 1
        list.append(x)
    else:
        x = 0
        list.append(x)
print(list)
