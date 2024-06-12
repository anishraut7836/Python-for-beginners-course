s = "Take up one idea and make that idea your life." \
    "Think and dream of that idea and leave every other idea alone."
subs = "idea"
found = False
pos = -1
length = len(s)
while True:
    pos = s. find(subs,pos+1,length)
    if pos == -1:
        break
    print("Found the sub string at position ",pos)
    found = True
if found == False:
    print("Sub String Not Found")


'''
Output:

Found the sub string at position  12
Found the sub string at position  31
Found the sub string at position  70
Found the sub string at position  97
'''

