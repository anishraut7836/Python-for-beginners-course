from random import *

print(random())


'''
Output:

0.4312080637581357
'''

#print 10 random number

from random import *

for i in range(10):
    print(random())



'''
Output:

0.5568899863809667
0.6713813420831641
0.3895332655430045
0.20951175839929004
0.26578613939067297
0.502812483796857
0.11165737507800377
0.7980470445010359
0.28256307773062683
0.6237290678751514

'''

#print random number in a range
from random import *

for i in range(10):
    print(randint(1,50))


'''
Output:

28
8
10
10
8
32
37
29
28
8
'''



#print random number in a range and exclude given number
from random import *

for i in range(10):
    print(uniform(1,50))



'''
Output:

11.442426459841046
34.69768405323317
49.36021712252194
10.683898794831345
5.056945250500787
28.438727685517172
8.74909777251047
17.311319087168016
10.056266069063343
4.5892992889999675
'''

#choice function

from random import *
list = ["java","python","devops","aws"]
for i in range(10):
    print(choice(list))


'''
Output:

aws
aws
python
java
java
devops
java
java
python
aws
'''