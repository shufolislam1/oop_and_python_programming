x = int(input())
sum = 0
for _ in range(x):
    a = int(input())
    b = int(input())
    for num in range(a+1,b):
        if num % 2 != 0:
            sum+= num
print(sum)    
