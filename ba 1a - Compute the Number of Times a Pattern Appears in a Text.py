txt = input()
ptrn = input()
cnt  = 0
for i in range(len(txt)):
    x  = txt[i:i+len(ptrn)]
    if(x == ptrn): 
        cnt+=1

print(cnt)
