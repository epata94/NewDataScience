def getTotalPage(m,n):
    totalPage = 0
    if m % n != 0:
        totalPage = m // n
        totalPage += 1
    else:
        totalPage = m // n

    return totalPage

print(getTotalPage(45, 10))