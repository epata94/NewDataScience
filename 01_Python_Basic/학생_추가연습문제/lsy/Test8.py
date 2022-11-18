def getTotalPage(m,n):
    if m==0:
        return 0
    return int((m-1)/n)+1

print(getTotalPage(5, 10)) # 1 출력
print(getTotalPage(15, 10)) # 2 출력
print(getTotalPage(25, 10)) # 3 출력
print(getTotalPage(30, 10)) # 3 출력