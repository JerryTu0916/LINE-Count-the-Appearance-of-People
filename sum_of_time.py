ifile = open("output_time.txt", 'rt', encoding='UTF-8')
ofile = open("output_time_sum.txt", 'wt', encoding='UTF-8')

c = ""
b = 'fuckfuckfuckfuckfuckfuckfuckfuckfuck'
flag = False
total_calls = 0

hr = 0
min = 0
sec = 0

while True:
    b = ifile.readline()
    count = 0

    if b == "":
        break
    total_calls += 1

    for char in b:
        if char == ':':
            count += 1

    if count == 1:
        if b[1] == ":":
            min += int(b[0])
        else:
            min += int(b[0:2])

    if count == 2:
        hr += int(b[0])
        min += int(b[2:4])

    sec += int(b[-2:])

min += int(sec/60)
sec %= 60
hr += int(min/60)
min %= 60

print("Total successful calls:", total_calls)
ofile.write("Total successful calls: " + str(total_calls))
print("total call time: " + str(int(hr/24)) + 'd ' + str(hr % 24) + 'hr ' + str(min) + 'min ' + str(sec) + 'sec')
ofile.write("\ntotal call time: ")
ofile.write(str(int(hr/24)) + 'd ' + str(hr % 24) + 'hr ' + str(min) + 'min ' + str(sec) + 'sec')

ofile.close()
ifile.close()