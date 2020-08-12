f = open("rosalind_ba1c.txt", "r")
line = f.readline()
f.close()
str = ""
for ch in line:
    if ch == 'A':
        com = 'T'
    elif ch == 'C':
        com = 'G'
    elif ch == 'G':
        com = 'C'
    elif ch == 'T':
        com = 'A'
    else: com = ''
    str = com + str
g = open('output.txt', 'w')
g.write(str)
g.close()
