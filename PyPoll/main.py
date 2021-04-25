# Add our dependencies.
import os
import csv


#import files
total_votes = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0
row_index = 0
candidate_options = []
candidate_name = ""
candidate_votes = {}
largest_county_turnout = ""
largest_county_vote = 0
county_votes = {}
county_names = []
county_name = []

# Open the election results and read the file.
with open('Resources/election_data.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1


    


with open("output","w") as txt_file:
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage}% ({votes})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    output = (
        f""" Election Results
        -------------------------
    
        Winner: {winning_candidate}
        Winning Vote Count: {winning_count}
        Winning Percentage: {winning_percentage}""")
    print(output)   
    txt_file.write(output)
