import numpy as np
def limb(D, n):
    lst = []
    for j in range(n):
        for k in range(n):
            if j != k:
                lst.append((D[n][k]+D[n][j]-D[j][k])/2)
    return min(lst)
def additivePhylogeny(D, n, interiorNode):
    neighbor = {}
    weight = {}
    if n == 2:
        neighbor[0] = [1]
        neighbor[1] = [0]
        weight[(0, 1)] = D[0][1]
        weight[(1, 0)] = D[0][1]
        return neighbor, weight, interiorNode
    limbLength = limb(D, n-1)
    for j in range(n-1):
        D[j][n-1] -= limbLength
        D[n-1][j] = D[j][n-1]
    iFound = -1
    kFound = -1
    for i in range(n-1):
        for k in range(n-1):
            if i != k:
                if D[i][k] == D[i][n-1] + D[n-1][k]:
                    iFound = i
                    kFound = k
                    break
        if iFound != -1 or kFound != -1:
            break
    x = D[iFound][n-1]
    neighbor, weight, interiorNode = additivePhylogeny(D[0:-1, 0:-1], n-1, interiorNode)
    # find path between iFound and kFound
    BFSqueue = [[iFound]]
    visited = set([iFound])
    path = []
    while len(BFSqueue) > 0:
        possiblePath = BFSqueue.pop()
        node = possiblePath[-1]
        visited.add(node)
        if node == kFound:
            path = possiblePath
            break
        for child in neighbor[node]:
            if child not in visited:
                BFSqueue.append(possiblePath + [child])
    # find the two nodes which the new node might be in the middle of them
    dist = 0
    leftNode, rightNode = 0, 0
    leftDist, rightDist = 0, 0
    for k in range(len(path) - 1):
        v, w = path[k], path[k + 1]
        if dist + weight[(v, w)] > x:
            leftNode, rightNode = v, w
            leftDist = x - dist
            rightDist = dist + weight[(v, w)] - x
            break
        dist += weight[(v, w)]
    node = leftNode
    if leftDist != 0:  # add new node to the tree
        node = interiorNode
        neighbor[leftNode].remove(rightNode)
        neighbor[rightNode].remove(leftNode)
        neighbor[leftNode].append(node)
        neighbor[rightNode].append(node)
        neighbor[node] = [leftNode, rightNode]
        weight[(node, leftNode)] = leftDist
        weight[(leftNode, node)] = leftDist
        weight[(node, rightNode)] = rightDist
        weight[(rightNode, node)] = rightDist
        del weight[(leftNode, rightNode)]
        del weight[(rightNode, leftNode)]
        interiorNode += 1
    # add leaf n to the tree
    neighbor[node].append(n-1)
    neighbor[n-1] = [node]
    weight[(n-1, node)] = limbLength
    weight[(node, n-1)] = limbLength
    return neighbor, weight, interiorNode
# main
n = 0
D = np.zeros((0, 0), dtype=np.int32)
with open("rosalind_ba7c.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            n = int(line)
            D = np.zeros((n, n), dtype=np.int32)
        else:
            rowData = np.array(line.split()).astype(np.int32)
            D[i-1] += rowData
neighbor, weight, _ = additivePhylogeny(D, n, n)
g = open('output.txt', 'w')
for i in sorted(neighbor):
    for j in sorted(neighbor[i]):
        g.write(str(i)+'->'+str(j)+':'+str(int(weight[(i, j)]))+'\n')