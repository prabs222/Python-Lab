import sys
sum=0
for i in range(len(sys.argv)):
    sum+=len(sys.argv[i])
print("The Sum of arguments is: " + str(sum))

