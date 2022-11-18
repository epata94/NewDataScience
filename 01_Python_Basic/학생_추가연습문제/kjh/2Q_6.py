def all_gugu(dan):
    if dan == "all":
        for i in range(2,10):
            for j in range(1,10):
                print(f"{i * j}\t", end="")
            print()

    else:
        dan = int(dan)
        for i in range(1,10):
            print(f"{dan*i}\t",end="")

dan = input("원하는 단을 입력하세요 : ")
all_gugu(dan)

