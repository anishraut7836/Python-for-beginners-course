l1 = eval(input('Enter a list of elements'))
s1 = set(l1)
print(s1)

#input example
#[10,20,30,10,30]
#it will remove the duplicate when print

#another method

l1 = eval(input('Enter a list of elements'))
print(l1)
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)
