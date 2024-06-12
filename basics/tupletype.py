tpl = (20,30,20,'xyz')
print(type(tpl))
print(tpl*3)
print(tpl.count(20))
print(tpl.index('xyz'))

#convert list into tuple
lst=[67,34,'xyz']
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)

##List vs Tuple
"""
#list       #tuple
[1,2,3]     (1,2,3)
Mutable     Immutable
Changing    Not Changing
Keys to Directory   Can be used
"""



