import os
inf = open("C:\\GitBox\\py_box\\Xmind\\input.txt", encoding='UTF-8')
outf = open("C:\\GitBox\\py_box\\Xmind\\output.txt", 'w', encoding='UTF-8')
ff = inf.readline()
while ff:
    length = len(ff)
    f = 0
    kg = 0
    jh = 0
    tt = 0
    for i in range(length):
        if ff[i:i+1] == '#':
            jh += 1
            if ff[i+1:i+2] == ' ':
                break
        elif ff[i:i+1] == "\t" and ff[i+1:i+2] == '-':
            kg = 1
            break
        elif ff[i:i+1] == '-' and ff[i+1:i+2] == ' ':
            f = 1
            break
        elif ff[i:i+1] == "\t" and ff[i+1:i+2] == "\t":
            tt = 1
            break

    if jh != 0:
        if jh == 1:
            ff = inf.readline()
            continue
        outf.write(ff[1:length])
        ff = inf.readline()
        continue

    if kg == 1 or tt == 1:
        outf.write(ff[1:length])
        ff = inf.readline()
        continue

    if f == 1:
        outf.write('###')
        outf.write(ff[1:length])
        ff = inf.readline()
        continue

    ff = inf.readline()
inf.close
outf.close
