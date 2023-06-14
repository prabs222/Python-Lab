# python program to find the max and min numbers in a list of integers
import random
list=[random.randint(1,i)  for i in range(1,100,10)]
print(list)
max=min=list[0]
for l in list:
    if l<min:
        min = l
    elif l > max:
        max = l
print("Maximum integer in list is: ",max)
print("Minimum integer in list is: ",min)
