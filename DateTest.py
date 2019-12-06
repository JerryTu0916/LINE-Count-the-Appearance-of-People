import matplotlib.pyplot as plt
import datetime

ifile = open("Chat with Shani.txt", "rt", encoding="UTF-8")
DateBuffer = ""

activity = 0
activities = []
Dates = []

while True:
    input = ifile.readline()
    activity += 1
    if input == '':
        break
    if input == '\n':
        DateBuffer = ifile.readline()
        DateBuffer = DateBuffer[:-5].split("/")
        if len(DateBuffer) == 3:
            Dates.append(DateBuffer)
            if activity > 1: activities.append(activity - 1)
            activity = 0

activities.append(activity)
activities.pop(0) #for some reason this needed to be done
mapping = {}

for i in range(min(len(Dates), len(activities))):
    if(tuple(Dates[i][:-1]) not in mapping.keys()):
        mapping[tuple(Dates[i][:-1])] = activities[i]
    else:
        mapping[tuple(Dates[i][:-1])] += activities[i]

a = []
for i in mapping.keys():
    t = datetime.date(int(i[0]), int(i[1]), 1)
    print(t)
    a.append(t.toordinal())

plt.plot_date(a, list(mapping.values()))
plt.show()
ifile.close()
