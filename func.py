# def fun1():
#     n = 3
#     print("the value of n is ",n)

# def fun2():
#     n = 5
#     print("the value of n is ",n)
#     fun1()
# fun2()

# n=10
# def fun1():
#     # n = 3
#     print("the value of n is ",n)

# def fun2():
#     n = 5
#     print("the value of n is ",n)
#     fun1()
# fun2()

# var = 10
# def fun1():
#     global var
#     var = var + 1
#     print("the value of n is ",var)
#     return
# fun1()

# def fun1(*arrgs):
#     # global var
#     # var = var + 1
#     for i in arrgs:
#         print(i)
#     print("New")
#     # print("the value of n is ",var)
#     return
# fun1(10,20,30)
# fun1(25,10,10,30,50,40)

def pat(n):
    for i in range(1,n):
        f=i+1
        for j in range(1,f):
            print("*")
        print("\n")
        # i+=1
        
pat(4)