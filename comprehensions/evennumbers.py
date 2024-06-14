lst=[x for x in range(2,21,2)]
print(lst)


'''
Output:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''


#another method

lst=[x for x in range(2,21) if x%2==0]
print(lst)

'''
Output:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''