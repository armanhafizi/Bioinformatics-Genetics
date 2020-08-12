def getNum(s:str, k:int):
    strNum = ''
    for i in range(k):
        if s[i] == 'A':
            strNum += '0'
        elif s[i] == 'C':
            strNum += '1'
        elif s[i] == 'G':
            strNum += '2'
        elif s[i] == 'T':
            strNum += '3'
    return int(strNum, base=4)
def getStr(m:int, k:int):
    s = ''
    n = m
    for i in range(k):
        if n % 4 == 0:
            s = 'A' + s
        elif n % 4 == 1:
            s = 'C' + s
        elif n % 4 == 2:
            s = 'G' + s
        elif n % 4 == 3:
            s = 'T' + s
        n = int(n/4)
    return s
#main
f = open("rosalind_ba3d.txt", "r")
k = int((f.readline())[0:-1]) - 1
text = (f.readline())[0:-1]
f.close()
ed = []
for i in range(4**k):
    ed.append([])
for i in range(len(text) - k):
    node = text[i:i+k]
    nextNode = text[i+1:i+k+1]
    ed[getNum(node, k)].append(nextNode)
g = open('output.txt', 'w')
for i in range(4**k):
    if len(ed[i]) != 0:
        g.write(getStr(i, k) + ' -> ')
        if len(ed[i]) == 1:
            g.write(ed[i][0] + '\n')
        else:
            g.write(ed[i][0])
            for l in ed[i]:
                if l != ed[i][0]:
                    g.write(',' + l)
            g.write('\n')
g.close()