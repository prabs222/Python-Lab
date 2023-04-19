n1 = int(input("Enter lower limit : "))
n2 = int(input("Enter upper limit :"))

for i in range(n1,n2+1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=1
            break
    if(c==0):
        print(i)
    
        