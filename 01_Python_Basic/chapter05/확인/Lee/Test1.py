def StarCount(height):
    star_count = 0
    for i in range(height):
        print('*' * (i+1))
        star_count += (i+1)
    return star_count

height=int(input("height: "))
print(f'star 개수:{StarCount(height)}')