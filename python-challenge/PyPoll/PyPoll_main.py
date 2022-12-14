# Dependencies
import csv

# Files to load and output
file_to_load = '/Users/abrahamofolu/Documents/GitHub/python-challenge/Resources/election_data.csv'
file_to_output = '/Users/abrahamofolu/Documents/GitHub/python-challenge/Analysis/PyPoll_output.txt'

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read in the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

# For each row
for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name for each row
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the date to out txt file
with open(file_to_output, "w") as txt_file:

# Print the final vote count
    output = "Election Results\n" + "-----------------------------\n" + "Total Votes:.format(total_votes\n)" + "------------------------------\n"

    print(output)

    # Save the final vote count to the txt file
txt_file.write(output)

# Determine the winner by looping through the counts
for candidate in candidate_votes:

        # Retrieve the vote count and candidate
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # Save each candidate's voter count and percentage to the txt file
        txt_file.write(voter_output)

# Print the winning candidate
winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-----------------------------\n"
)
print(winning_candidate_summary)

# Save the winning candidate's name to the txt file
txt_file.write(winning_candidate_summary)