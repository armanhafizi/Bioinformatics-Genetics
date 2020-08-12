from collections import defaultdict
#main
child = defaultdict(list)
inEdge = defaultdict(int)
E = 0
with open('rosalind_ba3m.txt') as openfileobject:
    for line in openfileobject:
        v, arrow, u = line.split()
        u = u.split(',')
        E += len(u)
        for ui in u:
            child[v].append(ui)
            inEdge[ui] += 1
paths = []
visited = []
for v in child:
    if not((v in inEdge) and inEdge[v] == 1 and len(child[v]) == 1):
        for w in child[v]:
            nonBranchingPath = [v, w]
            visited.append(v)
            visited.append(w)
            if (w in child) and (w in inEdge):
                while inEdge[w] == 1 and len(child[w]) == 1:
                    nonBranchingPath.append(child[w][0])
                    visited.append(child[w][0])
                    w = child[w][0]
                    if not(w in child and w in inEdge):
                        break
            paths.append(nonBranchingPath)
            E -= len(nonBranchingPath) - 1
while E > 0: #cycle left
    for v in child:
        if  not(v in visited):
            w = child[v][0]
            cyclicPath = [v, w]
            visited.append(v)
            while len(child[w]) == 1:
                if w in visited:
                    break
                cyclicPath.append(child[w][0])
                visited.append(w)
                w = child[w][0]
            paths.append(cyclicPath)
            E -= len(cyclicPath)
g = open('output.txt', 'w')
for p in paths:
    for i in range(len(p) - 1):
        g.write(p[i] + '->')
    g.write(p[-1] + '\n')
g.close()