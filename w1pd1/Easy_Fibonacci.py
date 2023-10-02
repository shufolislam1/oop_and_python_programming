x = int(input())
a=0
b=1
res = []
for num in range(x):
    res.append(a)
    temp = a
    a = b
    b = temp+b

print(" ".join(map(str, res)))
