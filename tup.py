str='1,2,3,4,5,6'
list=[int(i) for i in str.split(',')]
tup=(int(i) for i in str.split(','))
print('List =',list)
print('Tupple =',tuple(list))