try:
    file = open("life.txt", mode = 'r')
    str = file.read().replace('java', 'python')
    file = open("life.txt", mode = 'w', encoding='utf-8')
    file.write(str)
except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()
