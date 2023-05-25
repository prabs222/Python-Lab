file=open('hello.txt', 'r')
str=file.read()
words=str.split()
c=0
for word in words:
    if word=='hello':
        c+=1
print("number of 'hello' are ",c)