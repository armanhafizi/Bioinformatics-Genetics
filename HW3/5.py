from collections import defaultdict
def lastToFirst(text:str):
    return ''.join(sorted(text))
def firstOccurrence(symbol, first:str):
    for i in range(len(first)):
        if first[i] == symbol:
            return i
def count(symbol, top:int, lastColumn:str):
    num = 0
    global cnt
    if cnt[symbol][top] != -1:
        return cnt[symbol][top]
    for i in range(top):
        if i == len(lastColumn):
            break
        if lastColumn[i] == symbol:
            num += 1
    cnt[symbol][top] = num
    return num
def betterBWMatching(firstOccurrenceList:list, lastColumn:str, pattern:str):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[0:-1]
            if symbol in lastColumn[top:bottom + 1]:
                top = firstOccurrenceList[symbol] + count(symbol, top, lastColumn)
                bottom = firstOccurrenceList[symbol] + count(symbol, bottom + 1, lastColumn) - 1
            else:
                return 0
        else:
            return bottom - top + 1
#main
f = open('rosalind_ba9m.txt', 'r')
lastColumn = (f.readline())[0:-1]
pattern = (f.readline())[0:-1]
pattern = pattern.split()
f.close()
first = lastToFirst(lastColumn)
firstOccurrenceList = defaultdict(int)
firstOccurrenceList['$'] = firstOccurrence('$', first)
firstOccurrenceList['A'] = firstOccurrence('A', first)
firstOccurrenceList['G'] = firstOccurrence('G', first)
firstOccurrenceList['C'] = firstOccurrence('C', first)
firstOccurrenceList['T'] = firstOccurrence('T', first)
cnt = defaultdict(list)
cnt['$'] = [-1] * (len(lastColumn) + 1)
cnt['A'] = [-1] * (len(lastColumn) + 1)
cnt['C'] = [-1] * (len(lastColumn) + 1)
cnt['G'] = [-1] * (len(lastColumn) + 1)
cnt['T'] = [-1] * (len(lastColumn) + 1)
answer = []
for p in pattern:
    answer.append(betterBWMatching(firstOccurrenceList, lastColumn, p))
g = open('output.txt', 'w')
g.write(str(answer[0]))
for i in range(1, len(answer)):
    g.write(' ' + str(answer[i]))
g.close()