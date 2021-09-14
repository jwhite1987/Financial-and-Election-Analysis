import os

import csv

import sys


csvpath = os.path.join('Resources','budget_data.csv')
months = []
profits = []
difference = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    month = 0
    data = list(csvreader)
    month = len(data)
    total = 0
    for row in data:
        months.append(row[0])
        profits.append(row[1])
    for row in range(1,len(profits)):
        x = int(profits[row]) - int(profits[row - 1])
        difference.append(x)
    total = sum(int(row[1]) for row in data)
    maximum = max(int(i) for i in difference)
    minimum = min(int(i) for i in difference)
    for (a,b) in zip(months[1:], difference):
        if float(b) == minimum:
            minmonth = (a)
        if float(b) == maximum:
            maxmonth = (a)
    averagechange = round(sum(difference)/len(difference),2)
    stdoutOrigin=sys.stdout
    sys.stdout = open("Financial_Analysis.txt", "w")
    print('Financial Analysis\n----------------------------------------')
    print(f'Total Months: {month}')
    print(f'Total: ${total}')
    print(f'Average Change: ${averagechange}')
    print(f'Greatest Increase in Profits: {maxmonth} (${maximum})')
    print(f'Greatest Decrease in Profits: {minmonth} (${minimum})')
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    print('Financial Analysis\n----------------------------------------')
    print(f'Total Months: {month}')
    print(f'Total: ${total}')
    print(f'Average Change: ${averagechange}')
    print(f'Greatest Increase in Profits: {maxmonth} (${maximum})')
    print(f'Greatest Decrease in Profits: {minmonth} (${minimum})')
    # print(f'{profits}')
    # print(f'{data}')
