s=input()
print(s)
s=input("Enter your name:")
print(s)
i=int(input("Enter a integer number"))
print(i)
print(type(i))


#mutiple input from user end

lst = [x for x in input("Enter three numbers seprated by space:").split()]
print(lst)
print(type(lst))

lst = [x for x in input("Enter three numbers seprated by comma:").split(',')]
print(lst)
print(type(lst))


lst = [int(x) for x in input("Enter three numbers seprated by comma:").split(',')]
print(lst)
print(type(lst))

#float input example - 1.223,3.14,7.90
lst = [float(x) for x in input("Enter three numbers seprated by comma:").split(',')]
print(lst)
print(type(lst))

