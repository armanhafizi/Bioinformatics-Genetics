import collections
def readIn(fileName):
    n = 0
    c = 0
    label = collections.defaultdict(lambda: '')
    neighbor = collections.defaultdict(lambda: [])
    with open(fileName) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                n = int(line)
            else:
                x, y = line.split('->')
                if x[0] > '9':  # str->int
                    neighbor[c].append(int(y))
                    label[c] = x
                    c += 1
                elif y[0] > '9':  # int->str
                    deLabel = list(label.keys())[list(label.values()).index(y)]
                    neighbor[int(x)].append(deLabel)
                elif x[0] <= '9' and y[0] <= '9':  # int->int
                    neighbor[int(x)].append(int(y))
    return neighbor, label, n
def smallParsimony(neighbor, label, c):
    tag = {}
    s = {}
    charLabel = collections.defaultdict(lambda: 'X')
    riped = len(neighbor)
    for v in neighbor:
        s[v] = {}
        if len(neighbor[v]) == 1:  # leaf
            charLabel[v] = label[v][c]
            tag[v] = 1
            riped -= 1
            for k in ['A', 'C', 'G', 'T']:
                if k == label[v][c]:
                    s[v][k] = 0
                else:
                    s[v][k] = 1000000
        else:  # internal
            tag[v] = 0
    child = collections.defaultdict(lambda: [])
    parent = {}
    order = []
    while riped != 0:
        #print(s)
        v = 0
        for v in neighbor:
            if tag[v] == 0:
                for i in range(3):
                    if tag[neighbor[v][i]] == 1:
                        child[v].append(neighbor[v][i])
                if len(child[v]) == 2 or len(child[v]) == 3:  # has daughter and son
                    riped -= 1
                    break
        order.append(v)
        #print(v, child)
        tag[v] = 1
        for k in ['A', 'C', 'G', 'T']:
            s[v][k] = 0
            for ch in child[v]:
                parent[ch] = v
                m = []
                for i in ['A', 'C', 'G', 'T']:
                    m.append(s[ch][i] + (1 - int(k == i)))
                s[v][k] += min(m)
    #print(s, child, order)
    # backtrack
    order.reverse()
    score = 0
    for v in order:
        if v == order[0]:
            for k in ['A', 'C', 'G', 'T']:
                if s[v][k] == min(s[v].values()):
                    charLabel[v] = k
                    score = s[v][k]
                    break
        else:
            if s[v][charLabel[parent[v]]] - min(s[v].values()) <= 1:
                charLabel[v] = charLabel[parent[v]]
            else:
                for k in ['A', 'C', 'G', 'T']:
                    if s[v][k] == min(s[v].values()):
                        charLabel[v] = k
                        break
    return charLabel, score
def parsimony(neighbor, label):
    newLabel = collections.defaultdict(lambda: '')
    score = 0
    for i in range(len(label[0])):
        l, s = smallParsimony(neighbor, label, i)
        score += s
        for v in neighbor:
            newLabel[v] += l[v]
    return newLabel, score
def writeOut(neighbor, label, score):
    g = open('output.txt', 'w')
    g.write(str(score) + '\n')
    for v in neighbor:
        for w in neighbor[v]:
            hamDist = 0
            for i in range(len(label[0])):
                if label[v][i] != label[w][i]:
                    hamDist += 1
            g.write('%s->%s:%d\n' % (label[v], label[w], hamDist))
    g.close()
# main
neighbor, label, n = readIn('rosalind_ba7g.txt')
newLabel,  score = parsimony(neighbor, label)
writeOut(neighbor, newLabel, score)