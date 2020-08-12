def readIn(fileName):
    k = 0
    DNA = []
    n = 0
    with open(fileName) as f:
        for line in f:
            if n == 0:
                k = int(line[0:-1])
                n += 1
            else:
                DNA.append(line[0:-1])
                n += 1
    return k, DNA
def trans(n, k):
    s = ''
    for i in range(k):
        r = n % 4
        x = 0
        if r == 0:
            x = 'A'
        elif r == 1:
            x = 'C'
        elif r == 2:
            x = 'G'
        else:
            x = 'T'
        s = x + s
        n = int(n / 4)
    return s
def allWords(l):
    lst = []
    for i in range(4**l):
        lst.append(trans(i, l))
    return lst
def hamDist(v, w):
    n = 0
    for i in range(len(v)):
        if v[i] != w[i]:
            n += 1
    return n
def median(k, DNA):
    t = len(DNA)
    n = len(DNA[0])
    words = allWords(k)
    bestWord = words[0]
    bestDist = 1000000
    for w in range(1, len(words)):
        totDist = 0
        for j in range(t):
            bestSubDist = 1000000
            for i in range(n - k + 1):
                text = DNA[j][i:i+k]
                dist = hamDist(words[w], text)
                if dist < bestSubDist:
                    bestSubDist = dist
            totDist += bestSubDist
        if totDist < bestDist:
            bestDist = totDist
            bestWord = words[w]
    return bestWord, bestDist
def writeOut(bestWord):
    g = open('output.txt', 'w')
    g.write(str(bestWord))
    g.close()
# main
k, DNA = readIn('rosalind_ba2b.txt')
#print(k, DNA)
bestWord, bestDist = median(k, DNA)
writeOut(bestWord)