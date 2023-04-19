n = int(input("Enter a number to generate its factorial : "))
f = 1
for i in range(2,n+1):
    f*=i
print(f'Factorail of {n} is {f}')