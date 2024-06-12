s = input('Enter a string')
print(s[::-1])


#print the reverse world

s = input('Enter a string')
i = len(s)-1
result = ''
while i >= 0:
    result = result+s[i]
    i = i-1
print(result)

#input the world malayalam it will print the reverse but same word


#add , -, + 

s = input('Enter a string')
print('+'.join(reversed(s)))

#input bob
#output  b+o+b