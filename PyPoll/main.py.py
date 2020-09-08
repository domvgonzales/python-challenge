import os
import csv
election_csv = os.path.join('PyPoll','Resources','election_data.csv')

Total_Votes = []
Khan_Votes = []
Correy_Votes = []
Li_Votes = []
Otooley_Votes = []
with open(election_csv,'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)

  for row in csvreader:
      Total_Votes.append(row[0])
      County.append(row[1])
      Candidate.append(row[2])
        


print("Election Results")
print("--------------------")
print(f'Total_Votes: {len(Total_Votes)}')
print('--------------------')
print