with open('D:/Pywork/NewDataScience/01_Python_Basic\chapter08/data/ftest.txt', mode='r', encoding='utf-8') as ftest :
    # for i in range(6):
    #     line = ftest.readline()
    #     print(line.strip())
    print('\n\n')
    while True:
        line = ftest.readline()
        if line == '':
            break
        print(line.strip())
# exam01

mean()