inputFileName = input("please input the file name (please include .txt)\n")
outputFileName = "people count of {}".format(inputFileName)

inputFile = open(inputFileName, 'rt', encoding='UTF-8')

potentialName = ""
buffer = ''

people = {}
flag = False

while True:
    buffer = inputFile.readline()
    flag = False
    potentialName = ''

    if buffer == '':
        break

    for char in buffer:
        if char == '\t':
            if not flag:
                flag = True
            else:
                flag = False
                if not potentialName in people.keys():
                    people[potentialName] = 1
                else:
                    people[potentialName] += 1
        elif flag:
            potentialName += char

inputFile.close()

ofile = open(outputFileName, "wt", encoding="UTF-8")

total = 0
for ppl in people.keys():
    total += people[ppl]

for ppl in people.keys():
    print(ppl + ': ' + str(people[ppl]) + " (" +
          str(round(100*people[ppl]/total, 2)) + ' %)')
    ofile.write(ppl + ' : ' + str(people[ppl]) +
                " (" + str(round(100*people[ppl]/total, 2)) + ' %)\n')

print("================================")
print("total:", total)
ofile.write("================================\n")
ofile.write("total :" + str(total))

ofile.close()
