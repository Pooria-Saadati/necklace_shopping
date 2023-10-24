t = int(input())
x = list()
for i in range (0,t):
    a , b = input().split(" ")
    
    if len(a) == len(b):
        for j in range(0,len(a)):
            try:
                Index = b.index(a[j])
            except:
                Index = -2
            IsExist=0
            if Index < 0 :
                x.append("NO")
                IsExist = 1
                break
            else:
                b = b[:Index] + b[Index + 1:]
        if IsExist==0:
            x.append("YES")
    else : x.append("NO")    
    
    
for i in range(0,len(x)):
    print(x[i])