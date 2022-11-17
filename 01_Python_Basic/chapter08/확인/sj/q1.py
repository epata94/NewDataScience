try :
    file = open("test.txt", mode= 'r')
    print(file.read())
except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()



