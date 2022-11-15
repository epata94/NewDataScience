def StarCount(height):
    h_cnt = s_cnt = 0

    while h_cnt <height:
        h_cnt +=1
        print('*'*h_cnt)
        s_cnt +=  h_cnt

    return s_cnt

height = int(input("층의 개수를 입력하세요."))
print(StarCount(5))