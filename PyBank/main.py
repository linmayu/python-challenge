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
    print(f"CSV Header: {csv_header}")

#Calculate the total number of months included in the dataset
#Calculate the net total amount of "Profit/Losses" over the entire period
#Calculate the average of the changes in "Profit/Losses" over the entire period

    total_months = 0
    total_profit = 0
    change = []
    

    for row in csvreader:
        total_months = total_months + 1
        prev_profit = total_profit
        total_profit = total_profit + int(row[1])
        profit_change = total_profit - prev_profit
        change.append(profit_change)

print(change)
avg_change = sum(change) / len(change)
    




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
#print(change)
print(f"Average Change: {avg_change}")
#print(f"Greatest Increase in Profits: {greatest_increase}")
#print(f"Greatest Decrease in Profits: {greatest_decrease}")

#Export a text file with the analysis.