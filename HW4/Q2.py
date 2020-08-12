import numpy as np
def readIn():
    n = 0
    D = np.zeros((0, 0), dtype=np.int32)
    with open('rosalind_ba7d.txt') as f:
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
def UPGMA(D, n):
    parent = {}
    age = {i:0 for i in range(n)}
    clusterNum = {i:1 for i in range(n)}
    k = n-1  # new node counter
    while len(D) > 1:
        nearestDist = 1000000
        Ci, Cj = 0, 0
        for i in D:
            for j in D:
                if i != j and D[i][j] < nearestDist:
                    nearestDist = D[i][j]
                    Ci = i
                    Cj = j
        k += 1
        age[k] = float(nearestDist / 2)
        parent[Ci], parent[Cj] = k, k
        clusterNum[k] = clusterNum[Ci] + clusterNum[Cj]
        newD = {}
        for i in D:
            newD[i] = {}
            for j in D:
                newD[i][j] = D[i][j]
        del newD[Ci]
        del newD[Cj]
        for i in newD:
            del newD[i][Ci]
            del newD[i][Cj]
        newRow = {}
        for j in D:
            if j != Ci and j != Cj:
                newRow[j] = (D[Ci][j] * clusterNum[Ci] + D[Cj][j] * clusterNum[Cj]) / (clusterNum[Ci] + clusterNum[Cj])
        newRow[k] = 0
        newD[k] = newRow
        for i in D:
            if i != Ci and i != Cj:
                newD[i][k] = (D[i][Ci] * clusterNum[Ci] + D[i][Cj] * clusterNum[Cj]) / (clusterNum[Ci] + clusterNum[Cj])
        D = {}
        for i in newD:
            D[i] = {}
            for j in newD:
                D[i][j] = newD[i][j]
        #print(Ci, Cj)
        #print(clusterNum)
        #print(newD)
        #print('------------------------------------------------')
    return parent, age
def writeOut(parent, age):
    g = open('output.txt', 'w')
    adjList = []
    for node in parent:
        edge = round(age[parent[node]] - age[node], 3)
        adjList.append('%d->%d:%.3f\n' % (node, parent[node], edge))
        adjList.append('%d->%d:%.3f\n' % (parent[node], node, edge))
    for l in adjList:
        g.write(l)
    g.close()
# main
D, n = readIn()
parent, age = UPGMA(D, n)
writeOut(parent, age)