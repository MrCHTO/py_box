from os import write


def Basis():
    inf = open("C:\\GitBox\\py_box\\Xmind\\input.txt", encoding='UTF-8')
    outf = open("C:\\GitBox\\py_box\\Xmind\\output.txt", 'w', encoding='UTF-8')
    s = inf.readline()
    while s:
        length = len(s)
        a, b, c, d, e, f, g, h, x = 0, 0, 0, 0, 0, 0, 0, 0, 0
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

            elif s[i:i+1] == "\t" and s[i+1:i+2] == "\t" and s[i+2:i+3] == " ":
                x = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == "\t" and s[i+2:i+3] != " ":
                d = 1
                break

            elif s[i:i+1] == " " and s[i+1:i+2] == " " and s[i+2:i+3] != "\n":
                e = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == " " and s[i+3:i+4] != "\n":
                f = 1
                break

            elif s[i:i+1] != "\n" and s[i:i+1] != " " and s[i:i+1] != "\t":
                g = 1
                break

        if a != 0:
            if a == 1:
                s = inf.readline()
                continue
            if a == 2:
                outf.write('\n***\n')
            outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            continue

        if b == 1:
            outf.write('\n###')
            outf.write(s[1:length])
            s = inf.readline()
            continue

        if c == 1:
            outf.write('\n####')
            outf.write(s[2:length])
            s = inf.readline()
            continue

        if d == 1:
            if c == 1:
                outf.write('\n')
            outf.write(s[2:length])
            s = inf.readline()
            continue

        if e == 1:
            outf.write('>')
            outf.write(s[2:length])
            s = inf.readline()
            continue

        if f == 1:
            outf.write('>')
            outf.write(s[3:length])
            s = inf.readline()
            continue

        if g == 1:
            outf.write('>')
            outf.write(s[0:length])
            s = inf.readline()
            continue

        if x == 1:
            outf.write('\t>')
            outf.write(s[4:length])
            s = inf.readline()
            continue

        s = inf.readline()
    inf.close
    outf.close


def Picture():
    inf = open("C:\\GitBox\\py_box\\Xmind\\input.txt", encoding='UTF-8')
    outf = open("C:\\GitBox\\py_box\\Xmind\\output.txt", 'w', encoding='UTF-8')
    s = inf.readline()
    while s:
        length = len(s)
        a = 0
        for i in range(length):
            if s[i:i+1] == '!':
                if s[i+1:i+2] == '[':
                    a = 1
                    break

        if a == 1:
            outf.write(s[0:27])
            outf.write(s[97:length])
            s = inf.readline()
            continue
        else:
            outf.write(s)
        s = inf.readline()
    inf.close
    outf.close


def main():
    Basis()


if __name__ == '__main__':
    main()
