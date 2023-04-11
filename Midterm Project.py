# Step 1: Reading CSV file
import csv

dataList = []
with open ('data.csv', 'r') as file:
    data = csv.reader(file)
    for line in data:
        dataList.append(line)
        print(line)
file.close()

# Step 2: Total Sale
with open('data.csv', 'r') as file: #Read and record data
    data = csv.reader(file)
    firstLine = file.readline()
    total = {}
    for line in data:
        year = int(line[0])
        sales = line[1:]
        total[year] = sales
file.close()

for x in total: #turn data into totals
    sumValue = 0
    for y in range(len(total[x])):
        value = int(total[x][y])
        sumValue += value
    total[x] = sumValue

file = open('stats.txt','w') #write data to stats.txt
file.write("Year\tTotal Vehicles Sold\n")
for x in total:
    file.write(f"{x}\t{total[x]}\n")
file.close()

#Step 3: Bar Plot
import matplotlib.pyplot as plt

x = total.keys()
y = total.values()

plt.figure(1)
plt.bar(x,y)

plt.title("Vehicles Sold by Year")
plt.xlabel("Year")
plt.ylabel("Vehicles Sold")

plt.ticklabel_format(style='plain')
plt.show()

#Step 4: Sale Estimation
with open('data.csv', 'r') as file: #Read and record data
    data = csv.reader(file)
    firstLine = file.readline()
    total = {}
    for line in data:
        year = int(line[0])
        sales = line[1:]
        total[year] = sales
file.close()

for x in range(2012,2021): #remove unnecessary yrs
    if x != 2021 or 2022:
        total.pop(x)

total2021 = []
last2021 = []
for x in total: #convert data into usable info (totals for 2021 and 2022)
    for y in range(len(total[x])):
        value = int(total[x][y])
        if x == 2021 and y > 5:
            last2021.append(value)
    sumValue = 0
    for y in range(len(total[x])//2):
        value = int(total[x][y])
        sumValue += value
        if x == 2021:
            total2021.append(value)
    total[x] = sumValue

a = total[2022] #SGR calculation
b = total[2021]
SGR = (a-b)/a

estSales2022 = [] #Estimated sales for 2022
for i in range (6):
    est = last2021[i] + (last2021[i] * SGR)
    estSales2022.append(round(est))

months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

file = open('stats.txt','a') #writing data to stats.txt
file.write(f"\nSGR\t{SGR}\n")
file.write("\n")
file.write("Month\tEst Sales 2022\n")
for n in range(len(months)):
    file.write(f"{months[n]}\t\t{estSales2022[n]}\n")
file.close()

#Step 5 Horizontal Bar Plot
x = months
y = estSales2022

plt.figure(2)
plt.barh(x,y)

plt.title("Estimated Sales 2022")
plt.xlabel("Estimated Sales")
plt.ylabel("Month")

plt.show()






