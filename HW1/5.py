def mismatch(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count
#main
f = open("rosalind_ba1h.txt", "r")
pattern = f.readline()
pattern = pattern[0:-1]
text = f.readline()
text = text[0:-1]
k = f.readline()
k = k[0:-1]
k = int(k)
f.close()
l = len(pattern)
g = open('output.txt', 'w')
for i in range(len(text) - l):
    word = text[i:i + l]
    if mismatch(pattern, word) <= k:
        g.write(str(i) + ' ')
g.close()