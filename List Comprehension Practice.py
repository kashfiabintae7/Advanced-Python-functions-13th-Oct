number = input("Enter a number to know the odd ones: ").split()

numbers = [input(i) for i in input().split()]

odd = [number for number in numbers if number%2!=0]

print ("The odd numbers are: ", odd) 

#==========================================

fruits = ["apple", "mango", "banana", "kiwi", "tangerine"]

capfruit = [i.capitalize() for i in fruits]

print(capfruit)