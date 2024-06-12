s = 'aaaabbbbbcccczzzzzddddyyyysssiiiaaaggesssccc'
d = {}

for c in s:
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c] = 1
for k,v in d.items():
    print('{}={} times'.format(k,v))


'''
Output:

a=7 times
b=5 times
c=7 times
z=5 times
d=4 times
y=4 times
s=6 times
i=3 times
g=2 times
e=1 times
'''