import csv
import random
import time

xVal = 0
yVal1 = 1000
yVal2 = 1000

fieldNames = ["xVal", "yVal1", "yVal2"]

with open('data6.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
    csv_writer.writeheader()

while True:
    with open('data6.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

        info = {
            "xVal": xVal,
            "yVal1": yVal1,
            "yVal2": yVal2
            }

        csv_writer.writerow(info)
        print(xVal, yVal1, yVal2)

        xVal += 1
        yVal1 = yVal1 + random.randint(-6, 8)
        yVal2 = yVal2 + random.randint(-5, 6)

    time.sleep(1)
