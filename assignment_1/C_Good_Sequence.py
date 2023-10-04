t=int(input())
x=list(map(int, input().split()))
dictio = {}
for item in x:
    dictio[item] = 0
for item in x:
    dictio[item] += 1

result=0

for key, value in dictio.items():
    if value > key:
        result+= value-key
    elif value<key:
        result+=value

print(result)
