inf = []
def delete_intron(s: str):
    global inf
    start_pos = inf[0].find(s)
    end_pos = start_pos + len(s);
    inf[0] = (inf[0])[0:start_pos] + (inf[0])[end_pos:]
def transcript(s: str):
    trn = ''
    for i in s:
        if i == 'T':
            trn += 'U'
        else:
            trn += i
    return trn
def translate(s: str):
    prt = ''
    for i in range(int(len(s)/3)):
        sub = s[3*i:3*i+3]
        if sub[0:2] == 'GC':
           prt += 'A'
        elif sub[0:2] == 'CG' or sub == 'AGA' or sub == 'AGG':
            prt += 'R'
        elif sub == 'GAC' or sub == 'GAU':
            prt += 'D'
        elif sub == 'AAC' or sub == 'AAU':
            prt += 'N'
        elif sub == 'UGC' or sub == 'UGU':
            prt += 'C'
        elif sub == 'GAA' or sub == 'GAG':
            prt += 'E'
        elif sub == 'CAA' or sub == 'CAG':
            prt += 'Q'
        elif sub[0:2] == 'GG':
            prt += 'G'
        elif sub == 'CAC' or sub == 'CAU':
            prt += 'H'
        elif sub[0:2] == 'AU':
            if sub[2] == 'G':
                prt += 'M'
            else:
                prt += 'I'
        elif sub[0:2] == 'CU' or sub == 'UUA' or sub == 'UUG':
            prt += 'L'
        elif sub == 'AAA' or sub == 'AAG':
            prt += 'K'
        elif sub == 'UUC' or sub == 'UUU':
            prt += 'F'
        elif sub[0:2] == 'CC':
            prt += 'P'
        elif sub[0:2] == 'UC' or sub == 'AGC' or sub == 'AGU':
            prt += 'S'
        elif sub[0:2] == 'AC':
            prt += 'T'
        elif sub == 'UGG':
            prt += 'W'
        elif sub == 'UAC' or sub == 'UAU':
            prt += 'Y'
        elif sub[0:2] == 'GU':
            prt += 'V'
        else:
            break
    return prt
# main
with open('rosalind_splc.txt') as openfileobject:
    for line in openfileobject:
       if(line[0] == '>'):
           inf.append('')
       else:
           inf[-1] += line[0:-1]
for i in range(len(inf)-1):
    delete_intron(inf[i+1])
inf[0] = transcript(inf[0])
inf[0] = translate(inf[0])
g = open('output.txt', 'w')
g.write(inf[0])
g.close()