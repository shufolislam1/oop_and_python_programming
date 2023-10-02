x = int(input())

while x!= 0 :
    y = int(input())
    while True:
        print(y%10, end=" ")
        y //= 10
        if y == 0:
            break
    print()
    x-=1