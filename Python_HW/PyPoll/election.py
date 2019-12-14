import os

import csv

# set all vote totals to 0 
total_votes = 0
khan_votes = 0
otooley_votes = 0
correy_votes = 0
li_votes = 0

with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    #calculation for vote totals
    for row in csvreader:
        total_votes +=1
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

#Bring all calculations together and find highest total votes
candidates = ["Kahn", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Calculate percentages
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (otooley_votes/total_votes) *100

#Print all info out
print(f"Election Results")
print(f"-----------------")
print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"--------------------")
print(f"Winner: {key}")

with open("Election.txt", "w") as text_file:
    text_file.write(f"Election Results")
    text_file.write(f"-----------------")
    text_file.write(f"Total Votes: {total_votes}")
    text_file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    text_file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    text_file.write(f"Li: {li_percent:3f}% ({li_votes})")
    text_file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    text_file.write(f"--------------------")
    text_file.write(f"Winner: {key}")



















