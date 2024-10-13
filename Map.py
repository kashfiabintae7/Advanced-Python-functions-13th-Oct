lst = [1,2,3,4,5,6,7,8,9,10]

even = [i for i in lst if i%2==0]

print(even)

#=============================================

number = [4,5,4,7,8,9,5,6,2,1,3,6,5,8,99]

def sq(n):
    return n*n

res = map(sq,  number)

print(list(res))
#===============================================
num1 = [1,2,3,4,5,6,7,8]
num2 = [4,5,6,5,4,8,7,4]

sumList = map(lambda x,y: x+y , num1, num2)

print(list(sumList))