import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

# testing to convert data from string
#mydate = datetime.strpte('2018-07-01', '%Y-%m-%d')
# print(mydate)


dates = []
highs = []
lows = []
dates2 = []
highs2 = []
lows2 = []
names1 = []
names2 = []

for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        name1 = row[1]
    except ValueError:
        print(f"Missing Data for {the_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(the_date)
        names1.append(row[1])

for row in csv_file2:
    try:
        the_date2 = datetime.strptime(row[2], '%Y-%m-%d')
        high2 = int(row[5])
        low2 = int(row[6])
        name2 = row[1]
    except ValueError:
        print(f"Missing Data for {the_date2}")
    else:
        highs2.append(int(row[5]))
        lows2.append(int(row[6]))
        dates2.append(the_date2)
        names2.append(row[1])

# print(dates)
# print(highs)


fig = plt.figure()
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()

plt.show()


plt.subplot(2, 1, 1)
plt.title(names1[1], fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates2, highs2, c="red", alpha=0.5)
plt.plot(dates2, lows2, c="blue", alpha=0.5)

plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()

plt.subplot(2, 1, 2)
plt.title(names2[1], fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()


plt.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()
#row, column, index
