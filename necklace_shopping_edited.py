t = int(input())
x = list()

for i in range (0,t):
    a , b = input().split(" ")
    
    
    if len(a) == len(b):
        a
        for j in range(0,len(a)+1):
            a = a[1:] + a[0] 
            a2 = a[::-1]
            
            if a == b or a2 == b:
                x.append("YES")
                break
            a2 = a2[1:] + a2[0]
        else: x.append("NO")
    else: x.append("NO")

for i in range(0,len(x)):
    print(x[i])