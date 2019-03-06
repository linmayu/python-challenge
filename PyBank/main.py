#Import the budget_data.csv file

 # Import necessary dependencies
import os
import csv

# Create the path for the filename
csvpath = os.path.join("Resources", "budget_data.csv")

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    

#Calculate the total number of months included in the dataset
#Calculate the net total amount of "Profit/Losses" over the entire period
#Calculate the average of the changes in "Profit/Losses" over the entire period

    total_months = 0
    total_profit = 0
    profit = []
    change = []
    

    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        profit.append(int(row[1]))
        if len(profit) == 1:
            profit_change = profit[-1]
        else:
            profit_change = profit[-1] - profit[-2]
        change.append(profit_change)
        if change[-1] == max(change):
            best_month = row[0]
        elif change[-1] == min(change):
            worst_month = row[0]

avg_change = sum(change) / len(change)
greatest_increase = max(change)
greatest_decrease = min(change)
    




#Calculate the greatest increase in profits (date and amount) over the entire period

#Calculate the greatest decrease in losses (date and amount) over the entire period

#Print analysis to the terminal.  Analysis should look like the below:
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Profit: {total_profit}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {best_month} {greatest_increase}")
print(f"Greatest Decrease in Profits: {worst_month} {greatest_decrease}")

#Export a text file with the analysis.
f = open('financial_analysis.txt','w')
f.write("Financial Analysis" + os.linesep)
f.write("-------------------------" + os.linesep)
f.write(f"Total Months: {total_months}" + os.linesep)
f.write(f"Net Total Profit: {total_profit}" + os.linesep)
f.write(f"Average Change: {avg_change}" + os.linesep)
f.write(f"Greatest Increase in Profits: {best_month} {greatest_increase}" + os.linesep)
f.write(f"Greatest Decrease in Profits: {worst_month} {greatest_decrease}" + os.linesep)
f.close()