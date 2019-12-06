ifile = open("input.txt", 'rt', encoding='UTF-8')
ofile = open("output_time.txt", 'wt', encoding='UTF-8')

c = ""
b = '50m3b0dy h31p m3...'
flag = False

while True:
    b = ifile.readline()

    if b == '':
        break

    for char in b:
        if not ((char == "	") | (char == " ") | (char == "\n")):
            c += char
        else:
            if c == "通話時間":
                flag = True
            elif flag:
                flag = False
                ofile.write(c)
                ofile.write('\n')
            c = ""

ofile.close()
ifile.close()