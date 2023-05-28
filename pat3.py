n = int(input("Enter a number to generate a pattern : "))
f = 1
for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end='')  
    print()