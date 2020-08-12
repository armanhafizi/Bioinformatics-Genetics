import numpy as np
def readIn(fileName):
    n = 0
    D = np.zeros((0, 0), dtype=np.int32)
    with open(fileName) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                n = int(line)
                D = np.zeros((n, n), dtype=np.int32)
            else:
                rowData = np.array(line.split()).astype(np.int32)
                D[i - 1] += rowData
    dict = {}
    for i in range(n):
        dict[i] = {}
        for j in range(n):
            dict[i][j] = D[i][j]
    return dict, n
def neighborJoiningTree(D, n, interiorNode):
    neighbor = {}
    weight = {}
    if n == 2:
        for i in D:
            for j in D:
                if i != j:
                    neighbor[i] = [j]
                    weight[(i, j)] = D[i][j]
        return neighbor, weight, interiorNode
    totalDist = {}
    for i in D:
        totalDist[i] = 0
        for j in D:
            totalDist[i] += D[i][j]
    #print(totalDist)
    dPrime = {}
    for i in D:
        dPrime[i] = {}
        for j in D:
            if i != j:
                dPrime[i][j] = (n - 2) * D[i][j] - (totalDist[i] + totalDist[j])
            else:
                dPrime[i][j] = 0
    smallest = 1000000
    iSmall, jSmall = 0, 0
    for i in dPrime:
        for j in dPrime:
            if i != j and dPrime[i][j] < smallest:
                smallest = dPrime[i][j]
                iSmall = i
                jSmall = j
    #print(dPrime)
    #print(iSmall, jSmall)
    delta = (totalDist[iSmall] - totalDist[jSmall]) / (n - 2)
    limbLength = {}
    if delta >= 0:
        limbLength[iSmall] = (D[iSmall][jSmall] + delta) / 2.0
        limbLength[jSmall] = (D[iSmall][jSmall] - delta) / 2.0
    else:
        limbLength[iSmall] = (D[iSmall][jSmall] - delta) / 2.0
        limbLength[jSmall] = (D[iSmall][jSmall] + delta) / 2.0
    newD = {}
    for i in D:
        newD[i] = {}
        for j in D:
            newD[i][j] = D[i][j]
    del newD[iSmall]
    del newD[jSmall]
    for i in newD:
        del newD[i][iSmall]
        del newD[i][jSmall]
    newRow = {}
    for j in D:
        if j != iSmall and j != jSmall:
            newRow[j] = float((D[iSmall][j] + D[jSmall][j] - D[iSmall][jSmall]) / 2.0)
    newRow[interiorNode] = 0
    newD[interiorNode] = newRow
    for i in D:
        if i != iSmall and i != jSmall:
            newD[i][interiorNode] = float((D[i][iSmall] + D[i][jSmall] - D[iSmall][jSmall]) / 2.0)
    neighbor, weight, newInteriorNode = neighborJoiningTree(newD, n - 1, interiorNode + 1)
    neighbor[interiorNode].append(iSmall)
    neighbor[interiorNode].append(jSmall)
    neighbor[iSmall] = [interiorNode]
    neighbor[jSmall] = [interiorNode]
    weight[(iSmall, interiorNode)], weight[(interiorNode, iSmall)] = limbLength[iSmall], limbLength[iSmall]
    weight[(jSmall, interiorNode)], weight[(interiorNode, jSmall)] = limbLength[jSmall], limbLength[jSmall]
    #print(neighbor, weight, newInteriorNode)
    return neighbor, weight, newInteriorNode
def writeOut(neighbor, weight):
    g = open('output.txt', 'w')
    for i in sorted(neighbor):
        for j in sorted(neighbor[i]):
            g.write('%d->%d:%.3f\n' % (i, j, weight[(i, j)]))
# main
D, n = readIn('rosalind_ba7e.txt')
neighbor, weight, _ = neighborJoiningTree(D, n, n)
writeOut(neighbor, weight)