def comp(ch):
    if ch == 'A':
        return 'U'
    elif ch == 'U':
        return 'A'
    elif ch == 'G':
        return 'C'
    elif ch == 'C':
        return 'G'
def dp(i:int, j:int):
    global saved
    global RNA
    if i >= j:
        return 1
    if saved[i][j] != 0:
        return saved[i][j]
    ans = dp(i+1, j)
    for k in range(i+1, j+1):
        if(RNA[k] == comp(RNA[i])):
            ans += dp(i+1, k-1) * dp(k+1, j)
    saved[i][j] = ans
    return ans
RNA = ''
with open('rosalind_motz.txt') as openfileobject:
    for line in openfileobject:
       if(line[0] != '>'):
            RNA += line[0:-1]
l = len(RNA)
saved = [[0 for i in range(l)] for j in range(l)]
ans = dp(0, l-1)
g = open('output.txt', 'w')
g.write(str(ans%1000000))
g.close()