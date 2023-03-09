import csv
import os

current_dir = os.getcwd()
file_path_top = current_dir.split('python-challenge')[0]



# Establishing the file path for the source data.
file_path = file_path_top + "python-challenge\\PyPoll\\election_data.csv"



# Reads in the csv and establishes the variable data to be used later in the script. 
with open(file_path) as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip header row
    data = [row for row in csvreader]



# Calculates the total number of votes cast.
total_votes = len(data)



# Looks at the entire dataset to produce a list of unique candidates who received votes.
unique_candidates = list(set([row[2] for row in data]))



# Calculates the percentage of votes received by candidate.
candidate_vote_count = {candidate: 0 for candidate in unique_candidates}
for row in data:
    candidate = row[2]
    candidate_vote_count[candidate] += 1
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_vote_count.items()}



# Calculate the total number of votes won for each condidate.
candidate_votes = {candidate: 0 for candidate in unique_candidates}
for row in data:
    candidate = row[2]
    candidate_votes[candidate] += 1



# Determines the winner of the election based on the total votes cast.
winner = max(candidate_votes, key=candidate_votes.get)



# Print the results of the script.
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
for candidate in unique_candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------\n")



# Export the results to a text file.
with open('output.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate in unique_candidates:
        f.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")