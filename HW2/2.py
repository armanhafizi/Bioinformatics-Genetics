import urllib.request
def getSequence(s:str):
    seq = ''
    for line in s.splitlines():
        if line[0] != '>':
            seq += line
    return seq
def findMotif(s:str):
    loc = []
    for i in range(len(s)-3):
        if(s[i] == 'N' and s[i+1] != 'P' and (s[i+2] == 'S' or s[i+2] == 'T') and s[i+3] != 'P'):
           loc.append(i+1)
    return loc
# main
prtID = []
with open('rosalind_mprt.txt') as openfileobject:
    for line in openfileobject:
        prtID.append(line[0:-1])
g = open('output.txt', 'w')
for id in prtID:
    with urllib.request.urlopen('https://www.uniprot.org/uniprot/' + id + '.fasta') as url:
        s = url.read()
        s = s.decode("utf-8")
        s = getSequence(s)
        f = findMotif(s)
        if len(f) > 0:
            g.write(id + '\n')
            for l in f:
                g.write(str(l) + ' ')
            g.write('\n')
g.close()