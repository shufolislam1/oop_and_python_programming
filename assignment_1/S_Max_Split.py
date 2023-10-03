x=input()
cnt1=0
cnt2=0
ans=[]
cstr=""
for ch in x:
    if ch=='L':
        cnt1+=1
    else:
        cnt2+=1
    cstr+=ch
    if cnt1 == cnt2 :
        ans.append(cstr)
        cstr=""
print(len(ans))
for str in ans:
    print(str)