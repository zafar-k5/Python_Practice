### speed = (len * height) -1 * 9.8
import csv
with open(r"C:\gitstuff\Python_Practice\file_handling\ElephantHeights.csv","r") as EH:
    csv_reader = csv.reader(EH)
    fields = next(csv_reader)
    elephant_data = {}
    speed = []
    for elephant in csv_reader:
        if elephant[2] == "grey":
                elephant_data[elephant[0]] = [elephant[1]]


with open(r"C:\gitstuff\Python_Practice\file_handling\ElephantTypes.csv","r") as ET:
     csv_reader = csv.reader(ET)
     fields = next(csv_reader)
     for elephant in csv_reader:
          if elephant[0] in elephant_data:
               elephant_data[elephant[0]].append(elephant[1])

for key,value in elephant_data.items():
    speed.append(round((int(value[0]) * int(value[1])) - 1 * 9.8))

speed.sort(reverse=True)
print(speed)