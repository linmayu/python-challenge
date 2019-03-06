# Import necessary dependencies
import os
import csv

#Import the election_data.csv file

csvpath = os.path.join("Resources", "election_data.csv")

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    

    total_votes = 0
    candidates = []
    unique_list = []
    candidate_votes = 0
    unique_votes = []

    khan = []
    correy = []
    li = []
    o_tooley = []

#Calculate the total number of votes cast

    for row in csvreader:
        total_votes = total_votes + 1

        # Generate a complete list of candidates who received votes
        candidates.append(row[2])
        if row[2] == "Khan":
            khan.append(row[2])    
        elif row[2] == "Correy":
            correy.append(row[2])
        elif row[2] == "Li":
            li.append(row[2])
        else:
            o_tooley.append(row[2])

    for candidate in candidates:
        if len(unique_list) == 0:
            unique_list.append(candidate)
        elif candidate not in unique_list:
            unique_list.append(candidate)

#Show the percentage of votes each candidate won


#Show the total number of votes each candidate won

    khan_votes = len(khan)
    correy_votes = len(correy)
    li_votes = len(li)
    o_tooley_votes = len(o_tooley)

    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    o_tooley_percent = o_tooley_votes / total_votes



#Determine the winner of the election based on popular vote.

    results = [khan_votes, correy_votes, li_votes, o_tooley_votes]
    if max(results) == khan_votes:
        winner = "Khan"
    elif max(results) == correy_votes:
        winner = "Correy"
    elif max(results) == li_votes:
        winner = "Li"
    else:
        winner = "O'Tooley"
    

#Print the analysis to the terminal and generate a text file with the results.  It should look like the one below:

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_percent:.3%} ({khan_votes})")
print(f"Correy: {correy_percent:.3%} ({correy_votes})")
print(f"Li: {li_percent:6.3%} ({li_votes})")
print(f"O'Tooley: {o_tooley_percent:6.3%} ({o_tooley_votes})")
print(f"Winner: {winner}")

#Export a text file with the analysis.
f = open('election_results.txt','w')
f.write("Election Results" + os.linesep)
f.write("-------------------------" + os.linesep)
f.write(f"Total Votes: {total_votes}" + os.linesep)
f.write(f"Khan: {khan_percent:.3%} ({khan_votes})" + os.linesep)
f.write(f"Correy: {correy_percent:.3%} ({correy_votes})" + os.linesep)
f.write(f"Li: {li_percent:6.3%} ({li_votes})" + os.linesep)
f.write(f"O'Tooley: {o_tooley_percent:6.3%} ({o_tooley_votes})" + os.linesep)
f.write(f"Winner: {winner}" + os.linesep)
f.close()