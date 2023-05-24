a=int(input("Enter a number : "))
b=int(input("Enter second number : "))
n=min(a,b)
m=max(a,b)
r=m%n
if(r==0):
    print(n)
else:
    m=n
    n=r
    while(r!=0):
        r=m%n
        if(r!=0):
            m=n
            n=r
    print(n)    
