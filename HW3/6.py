def mismatch(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count
#main
f = open("rosalind_ba9o.txt", "r")
text = (f.readline())[0:-1]
pattern = (f.readline())[0:-1]
pattern = pattern.split()
k = int((f.readline())[0:-1])
f.close()
position = []
for p in pattern:
    l = len(p)
    for i in range(len(text) - l + 1):
        word = text[i:i + l]
        if mismatch(p, word) <= k:
            position.append(str(i))
position.sort()
g = open('output.txt', 'w')
g.write(position[0])
for i in range(1, len(position)):
    g.write(' ' + position[i])
g.close()