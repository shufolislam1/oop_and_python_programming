
t = int(input())
x = list(map(int, input().split()))

cnt = 0
ev=True
while ev:
    for num in range(t):
        if x[num]%2 != 0:
            ev=False
            break
        else:
            x[num]= x[num]//2
    cnt+=1
ev = False
print(cnt-1)