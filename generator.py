# use this file first before everything else

peopleCount = int(input("Please enter the amount of people; 2 if used to count private message"))
people = []

for i in range(peopleCount):
    inputBuffer = input("input #{}: ".format(str(i + 1)))
    people.append(inputBuffer)

print(people)

ifile = open("template", "rt")
ofile = open("generated_file.py", "wt")

for i in range(9):
    ofile.write(ifile.readline())

ofile.write("people = {")

for i in people:
    ofile.write("'{}': 0, ".format(i))

ofile.write("'placeholder': 0}\n")

for line in ifile:
    ofile.write(line)

ifile.close()
ofile.close()