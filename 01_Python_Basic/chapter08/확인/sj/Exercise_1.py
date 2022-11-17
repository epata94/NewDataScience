
try :
    file = open("./ftest.txt", mode = 'r')

    lines = file.readlines()

    docs = []

    words = []

    for line in lines :
        docs.append(line.strip())
        for word in line.split() :
            words.append(word)

    print('문장 내용')
    print(docs)
    print(f'문장 수 : {len(docs)}')

    print('단어 내용')
    print(words)
    print(f'단어 수 : {len(words)}')

except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()
