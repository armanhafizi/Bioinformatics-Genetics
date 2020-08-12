f = open("rosalind_ba1d.txt", "r")
substr = f.readline()
substr = substr[0:-1]
line = f.readline()
line = line[0:-1]
f.close()
i = 0
g = open('output.txt', 'w')
while i < len(line):
    s = line[i:]
    if substr in s:
        g.write(str(s.index(substr) + i) + ' ')
        i = s.index(substr) + i + 1
    else: break
g.close()