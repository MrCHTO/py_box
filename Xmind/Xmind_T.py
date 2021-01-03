def Basis():
    inf = open("C:\\GitBox\\py_box\\Xmind\\input.txt", encoding='UTF-8')
    outf = open("C:\\GitBox\\py_box\\Xmind\\output.txt", 'w', encoding='UTF-8')
    s = inf.readline()
    while s:
        length = len(s)
        a, b, c, d = 0, 0, 0, 0
        for i in range(length):
            if s[i:i+1] == '#':
                a += 1
                if s[i+1:i+2] == ' ':
                    break
            elif s[i:i+1] == '-' and s[i+1:i+2] == ' ':
                b = 1
                break
            elif s[i:i+1] == "\t" and s[i+1:i+2] == '-':
                c = 1
                break
            elif s[i:i+1] == "\t" and s[i+1:i+2] == "\t":
                d = 1
                break

        if a != 0:
            if a == 1:
                s = inf.readline()
                continue
            outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            continue

        if b == 1:
            outf.write('\n')
            outf.write('###')
            outf.write(s[1:length])
            s = inf.readline()
            continue

        if c == 1 or d == 1:
            outf.write(s[1:length])
            s = inf.readline()
            continue

        s = inf.readline()
    inf.close
    outf.close
    return
