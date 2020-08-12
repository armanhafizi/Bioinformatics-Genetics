import math
RNA = ''
with open('rosalind_mmch.txt') as openfileobject:
    for line in openfileobject:
       if(line[0] != '>'):
            RNA += line[0:-1]
A_num = 0
C_num = 0
U_num = 0
G_num = 0
for ch in RNA:
    if ch == 'A':
        A_num += 1
    elif ch == 'C':
        C_num += 1
    elif ch == 'U':
        U_num += 1
    elif ch == 'G':
        G_num += 1
#print(A_num, U_num, C_num, G_num)
if U_num > A_num:
    U_num, A_num = A_num, U_num
if G_num > C_num:
    C_num, G_num = G_num, C_num
one = 1
for i in range(U_num):
    one *= i + A_num - U_num + 1
two = 1
for i in range(G_num):
    two *= i + C_num - G_num + 1
ans = one * two
g = open('output.txt', 'w')
g.write(str(int(ans)))
g.close()