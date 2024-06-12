s = 'abcdddsssttttXXXXZZZIIippP'
temp = []
for c in s:
    if c not in temp:
        temp.append(c)
print(temp)
output = ' '.join(temp)
print(output)


'''
Output:

['a', 'b', 'c', 'd', 's', 't', 'X', 'Z', 'I', 'i', 'p', 'P']
a b c d s t X Z I i p P
'''