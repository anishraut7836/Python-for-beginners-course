n = int(input('Enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()

"""
Input : 7

Output:

Enter the number of rows
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
"""

n = int(input('Enter the number of rows'))
for i in range(1, n+1):
    print("# "*i) 


"""
input : 10

Output:

Enter the number of rows
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # # 
# # # # # # # # 
# # # # # # # # # 
# # # # # # # # # #

"""