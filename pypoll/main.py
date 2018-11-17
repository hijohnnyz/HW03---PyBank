import os
import csv

election_data_csv = os.path.join("election_data.csv")

with open(election_data_csv) as f:
    reader = csv.reader(f)
    row = next(reader, None)
    total_votes = 0
    list_candidates = []
    ind_votes = []

    for row in reader:

        total_votes += 1
        candidate = row[2]

        if candidate in list_candidates:
            candidate_index = list_candidates.index(candidate)
            ind_votes[candidate_index] = ind_votes[candidate_index] + 1
        else:
            list_candidates.append(candidate)
            ind_votes.append(1)

            percent = []
            high_votes = ind_votes[0]
            high_index = 0

        for count in range(len(list_candidates)):
            vote_percent = round(int(ind_votes[count]) / total_votes * 100, 3)
            percent.append(vote_percent)
            if ind_votes[count] > high_votes:
                high_votes = ind_votes[count]
                high_index = count
            winner = list_candidates[high_index]

print(f"Here are the election results: ")
print(f"------------------------------")
print(f'Total votes = {total_votes}')
print(f"------------------------------")
for count in range(len(list_candidates)):
    print(f'{list_candidates[count]}: {percent[count]}% ({ind_votes[count]})')
print(f"------------------------------")
print(f'Winner is: {winner}')
print(f"------------------------------")

write_file = f"pypoll_results.txt"
filewriter = open(write_file, mode = 'w')
filewriter.write(f"Election Results for PyPoll:\n")
filewriter.write("---------------------------\n")
filewriter.write((f"Total votes: {total_votes} votes cast\n"))
for count in range(len(list_candidates)):
    filewriter.write(f"{list_candidates[count]}: {percent[count]}% ({ind_votes[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

filewriter.close()