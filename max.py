str=input()
words=str.split()
max=0
largest=''
for word in words:
    if (len(word)>max):
        max=len(word)
        largest=word
print('max=',largest)