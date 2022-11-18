cnt = tot = 0
sum = []

# while cnt < 999:
while cnt < 999:
    cnt += 1

    if cnt%3 == 0 or cnt%5 == 0:
        tot += cnt
        sum.append(cnt)

print(tot)