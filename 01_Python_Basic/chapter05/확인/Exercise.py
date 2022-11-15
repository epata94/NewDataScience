#[문제1]

def StarCount(height) :

    count = 0;

    for i in range(height):
        for j in range(i+1):
            print('*', end='')
            count+=1
        print()

    return count

height = int(input('height : '))

print(f'star 개수 : {StarCount(height)}')