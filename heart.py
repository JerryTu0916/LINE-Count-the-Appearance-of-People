#doesn't work with Obfuscated.txt

inputFileName = input("please input file name (please include '.txt')")

ifile = open(inputFileName, 'rt', encoding='UTF-8')
ofile = open("output_heart.txt", 'wt', encoding='UTF-8')

b = 'd0wnw4rd 5p!r41 -- emp'

hearts = "♥💖💗💓💙💚💛💜🧡💞💟🖤❤💕"
hearts_desc = ["heart_suit", "sparking_heart", "glowing_heart",
               "beating_heart", "blue_heart", "green_heart",
               "yellow_heart", "purple_heart", "orange_heart",
               "revolving_hearts", "heart_decoration", "black_heart",
               "red_heart", "two_hearts"]

hearts_count = []

for i in hearts:
    hearts_count.append(0)

while True:
    b = ifile.readline()

    if b == "":
        break

    for char in b:
        index = 0
        for heart in hearts:
            if char == heart:
                hearts_count[index] += 1
            index += 1

index = 0
for heart in hearts:
    print(heart + hearts_desc[index] + ": " + str(hearts_count[index]))
    ofile.write(heart + hearts_desc[index] + ": " + str(hearts_count[index]) + "\n")
    index += 1

total = 0
for i in hearts_count:
    total += i

print(total)
ofile.write("\ntotal: " + str(total))

ofile.close()
ifile.close()