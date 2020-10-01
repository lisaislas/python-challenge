#PyBank csv script
import os
import csv

#file path
csvpath = os.path.join("budget_data.csv")

#declare vairables
months = 0
total_profit_loss = 0
changes = []
count = 0
greatest_increase_date = " "
greatest_decrease_date = " "

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Count months in data
    for row in csvreader:
        print(row[1])
        months = months + 1
        pnl = int(row[1])
        total_profit_loss = total_profit_loss + pnl
        changes.append(int(row [1]))
        greatest_increase_date = max(greatest_increase_date)
        greatest_decrease_date = min(greatest_decrease_date)
        count = count + 1



report = f'''
Financial Analysis
----------------------------
Total Months: {months} 
Total: ${total_profit_loss}
# Average Change: $ {sum(changes)/count} -2315.12
# Greatest Increase in Profits: max{greatest_increase_date} Feb-2012 ($1926159)
# Greatest Decrease in Profits: min{greatest_decrease_date} Sep-2013 ($-2196167)
'''

print(report)

#textfile
file = os.path.join("budget_data.txt")

with open (file, 'w') as text:
    print(text)

    lines = text.read()
    print (lines)