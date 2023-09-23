#dependencies
import os
import csv

# files to retrieve and output
ELECTION_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("Analysis","election_data.csv")
CANDIDATE_COL = 2
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# initialize the voter parameters
total_votes_cast = 0
candidate_votes = {}
winning_votes = 0
winning_candidate = ""

with open(ELECTION_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        # read header row before reading the data
        header = next(reader)
        for row in reader:
            # count the total votes cast
            total_votes_cast += 1
            current_name = row[CANDIDATE_COL]
            
            #use the library to add up each candidates vote count
            if current_name in candidate_votes:
                candidate_votes[current_name] +=1
            else:
                candidate_votes[current_name] = 1
                
        # find percentage of votes each candidate won.
        for candidate in candidate_votes:
            votes = candidate_votes.get(candidate)
            print (candidate)
            print(votes)
            candidate_percent=(votes/total_votes_cast*100)
            
            if votes > winning_votes:
                winning_votes = votes
                winning_candidate = candidate


text = (f" \n"
f" Election Results \n"
"  \n"
"---------------------------------  \n"
f" Total Votes: {total_votes_cast} \n"
f"---------------------------------  \n"
#f"  \n"
f" {candidate_votes} \n"
f"  \n"
f"---------------------------------  \n"
f"{candidate}:  {candidate_percent:.3f}%  ({votes}) \n"
"---------------------------------  \n"
" \n"
"---------------------------------  \n"
f" Winner: {winning_candidate} \n"
"---------------------------------  \n")

print(text)

#Export the analysis test 
with open(OUTPUT_PATH,"w") as txt_file:
    txt_file.write(text)
    
                        
#JUST CHECKING the totals
#print(candidate_votes)
#print (total_votes_cast)
#print ("---winner---")
#print (winning_votes)
#print (winning_candidate)
#print (candidate_percent)