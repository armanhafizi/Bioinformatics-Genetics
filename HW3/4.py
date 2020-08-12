f = open('rosalind_ba9i.txt', 'r')
text = (f.readline())
f.close()
row = []
row.append(text)
for i in range(len(text) - 1):
    text = text[-1] + text[0:-1]
    row.append(text)
row.sort()
BWM = ''
for i in row:
    BWM += i[-1]
g = open('output.txt', 'w')
g.write(BWM)
g.close()