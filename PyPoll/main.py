import os

import csv

import sys

csvpath = os.path.join('Resources','election_data.csv')
votes = []
winner = []
winnername = ["Khan", "Correy", "Li", "O'Tooley"]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)
    totalvotes = len(data)
    khantotal= 0
    litotal = 0
    correytotal = 0
    otooleytotal = 0
    for row in data:
        votes.append(row[2])
    for count in votes:
        if count == 'Khan':
            khantotal += 1
        elif count == 'Correy':
            correytotal += 1
        elif count == 'Li':
            litotal += 1
        else:
            otooleytotal += 1
    winner.append(khantotal)
    winner.append(correytotal)
    winner.append(litotal)
    winner.append(otooleytotal)
    maxvote = max(winner)
    for (a,b) in zip(winnername, winner):
        if float(b) == maxvote:
            winnername = (a)
    stdoutOrigin=sys.stdout
    sys.stdout = open("Election_Results.txt", "w")
    print('Election Results\n----------------------------')
    print(f'Total Votes: {totalvotes}\n----------------------------')
    khanpercentage = "{:.2%}".format(khantotal/totalvotes)
    print(f'Khan: {khanpercentage} ({khantotal})')
    correypercentage = "{:.2%}".format(correytotal/totalvotes)
    print(f'Correy: {correypercentage} ({correytotal})')
    lipercentage = "{:.2%}".format(litotal/totalvotes)
    print(f'Li: {lipercentage} ({litotal})')
    otooleypercentage = "{:.2%}".format(otooleytotal/totalvotes)
    print(f"O'Tooley: {otooleypercentage} ({otooleytotal})")
    print('----------------------------')
    print(f'Winner: {winnername}')
    print('----------------------------')
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    print('Election Results\n----------------------------')
    print(f'Total Votes: {totalvotes}\n----------------------------')
    khanpercentage = "{:.2%}".format(khantotal/totalvotes)
    print(f'Khan: {khanpercentage} ({khantotal})')
    correypercentage = "{:.2%}".format(correytotal/totalvotes)
    print(f'Correy: {correypercentage} ({correytotal})')
    lipercentage = "{:.2%}".format(litotal/totalvotes)
    print(f'Li: {lipercentage} ({litotal})')
    otooleypercentage = "{:.2%}".format(otooleytotal/totalvotes)
    print(f"O'Tooley: {otooleypercentage} ({otooleytotal})")
    print('----------------------------')
    print(f'Winner: {winnername}')
    print('----------------------------')
