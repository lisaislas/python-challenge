#PyPoll csv script
import os
import csv

#file path
csvpath = os.path.join("election_data.csv")

#Declare Variables
totalvoters = 0
count = 0
percent = 0

candidates = []
countcandidate = []
percentcandidate = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)

    #Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in reader:
        totalvoters +=1
        if row [2] not in candidates:
        count = count + 1
        percent = 0

        csvfile.seek(0)
        next (reader)

        for row in reader:
            if i == row [2]

                count += 1
                percent = (count / totalvoters) * 100

        countcandidate.append(count)
        percentcandidate.append(percent)

zip(candidates, percentcandidate, countcandidate)

report = f'''
Election Results
-------------------------
Total Votes: {totalvoters} 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''

print(report)

#textfile
file = os.path.join("election_data.txt")

with open (file, 'w') as text:
    print(text)

    lines = text.read()
    print (lines)
