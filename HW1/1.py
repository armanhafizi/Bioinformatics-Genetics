f = open("rosalind_dna.txt", "r")
line = f.readline()
f.close()
A_num = 0
C_num = 0
G_num = 0
T_num = 0
for ch in line:
    if ch == 'A':
        A_num += 1
    if ch == 'C':
        C_num += 1
    if ch == 'G':
        G_num += 1
    if ch == 'T':
        T_num += 1
g = open('output.txt', 'w')
g.write(str(A_num) + ' ' + str(C_num) + ' ' + str(G_num) + ' ' + str(T_num))
g.close()