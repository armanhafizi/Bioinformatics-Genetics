import math
RNA = ''
with open('rosalind_pmch.txt') as openfileobject:
    for line in openfileobject:
       if(line[0] != '>'):
            RNA += line[0:-1]
A_num = 0
C_num = 0
for ch in RNA:
    if ch == 'A':
        A_num += 1
    elif ch == 'C':
        C_num += 1
g = open('output.txt', 'w')
g.write(str(math.factorial(A_num)*math.factorial(C_num)))
g.close()