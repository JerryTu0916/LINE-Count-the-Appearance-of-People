#doesn't work with Obfuscated.txt
inputFileName = input("please input file name (please include '.txt')")

ifile = open(inputFileName, 'rt', encoding='UTF-8')
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
            if c == "通話時間": # doesn't work with any other language other then 'ZH-TW'
                flag = True
            elif flag:
                flag = False
                ofile.write(c)
                ofile.write('\n')
            c = ""

ofile.close()
ifile.close()