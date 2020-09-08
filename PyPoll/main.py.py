import os
import csv
election_csv = os.path.join('PyPoll','Resources','election_data.csv')

Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
Otooley_Votes = 0

with open(election_csv,'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)

  for row in csvreader:
        Total_Votes +=1

        if row[2] == "Khan":
            Khan_Votes +=1
        elif row[2] == "Correy":
            Correy_Votes +=1
        elif row[2] == "Li": 
            Li_Votes +=1
        elif row[2] == "O'Tooley":
            Otooley_Votes +=1

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [Khan_Votes, Correy_Votes, Li_Votes, Otooley_Votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key =dict_candidates_and_votes.get)

Khan_Percent = (Khan_Votes/Total_Votes) *100
Correy_Percent = (Correy_Votes/Total_Votes) * 100
Li_Percent = (Li_Votes/Total_Votes)* 100
Otooley_Percent = (Otooley_Votes/Total_Votes) * 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {Total_Votes}")
print(f"----------------------------")
print(f"Khan: {Khan_Percent:.3f}%({Khan_Votes})")
print(f"Correy: {Correy_Percent:.3f}% ({Correy_Votes})")
print(f"Li: {Li_Percent:.3f}% ({Li_Votes})")
print(f"O'Tooley: {Otooley_Percent:.3f}% ({Otooley_Votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

