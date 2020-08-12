from collections import defaultdict
#main
child = defaultdict(list)
inEdge = defaultdict(int)
with open('rosalind_ba3g.txt') as openfileobject:
    for line in openfileobject:
        v, arrow, u = line.split()
        u = u.split(',')
        for ui in u:
            child[v].append(ui)
            inEdge[ui] += 1
for v in child:
    if len(child[v]) == inEdge[v] + 1:
        break
stack = []
path = []
currentNode = v
while True:
    if not (currentNode in child):
        path.append(currentNode)
        currentNode = stack[-1]
        stack = stack[0:-1]
    else:
        stack.append(currentNode)
        oldNode = currentNode
        currentNode = child[currentNode][-1]
        child[oldNode] = child[oldNode][0:-1]
        if len(child[oldNode]) == 0:
            del child[oldNode]
    if len(stack) == 0 and not(oldNode in child):
        path.append(currentNode)
        break
path.reverse()
g = open('output.txt', 'w')
for i in range(len(path) - 1):
    g.write(path[i] + '->')
g.write(path[-1])
g.close()