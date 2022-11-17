with open("message.txt","w",encoding="UTF-8") as file:
    for i in range(1,11):
        file.write(f'파이팅{i}\n')

    file.close()