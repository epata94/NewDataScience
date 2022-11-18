def getTotalPage(m,n):
    if m %10 == 0:
        page_num = m//n
        return page_num
    else:
        page_num = m//n + 1
        return page_num

number = input("게시물 총 건수와 페이지당 보여줄 게시물을 입력하세요 (예 5,10)")
check = number.find(',')
#print(check)
m = int(number[:check])
n = int(number[check+1:])
#print(type(m))
#print(type(n))
print(f"출력: {getTotalPage(m,n)}")
