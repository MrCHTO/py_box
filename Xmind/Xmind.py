import os


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
            outf.write(s[1:length])
            s = inf.readline()
            continue

        if b == 1:
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
    # Basis()
    Picture()


if __name__ == '__main__':
    main()
