s = 'All the power is with in you'
temp = s.split()
print(temp)

#output
##['All', 'the', 'power', 'is', 'with', 'in', 'you']

s = 'All the power is with in you'
temp = s.split()
print(temp)
result = []
i = len(temp)-1
while i >= 0:
    result.append(temp[i])
    i = i-1
print(result)
output = ' '.join(result)
print(output)

#it will print the output in reserved order
"""
Output:

['All', 'the', 'power', 'is', 'with', 'in', 'you']
['you', 'in', 'with', 'is', 'power', 'the', 'All']
you in with is power the All
"""


