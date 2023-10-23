t = int(input())
x = list()
for i in range (0,t):
    a , b = input().split(" ")
    
    if len(a) == len(b):
        for j in range(0,len(a)):
            
            if b.find(a[j]) < 0 :
                x.append("NO")
                break
        else : x.append("YES")
    else : x.append("NO")    
    
    
for i in range(0,len(x)):
    print(x[i])