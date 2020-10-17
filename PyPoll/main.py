import os
import csv

vote_dict ={}
votes_per_candidate={}

csvpath = ("Resources\election_data.csv")
with open (csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next (csvreader)

    for row in csvreader:
        vote_dict[int(row[0])]=row[2]
    
    votes_cast = len(vote_dict) #number of votes cast
    candidates = set(vote_dict.values()) #list of candidates

    for candidate in candidates:
        #summing votes for each candidate from the list generated
        #from the candidates list above
        votes_per_candidate[candidate] = sum(value == candidate for value in vote_dict.values())

#write to terminal
    print ("Election Results")
    print ("-------------------------")
    print (f"Total Vote: {votes_cast}")
    print ("-------------------------")

    for key, value in votes_per_candidate.items():
        print (f"{key} {round((value/votes_cast *100),2)}% ({value})")
    print ("-------------------------")
    print (f"Winner: {max(votes_per_candidate,key=votes_per_candidate.get)}")


#write to a file
    f = open("PyPoll_Results.txt", "x")
    f.write ("Election Results")
    f.write ("\n-------------------------")
    f.write (f"\nTotal Vote: {votes_cast}")
    f.write ("\n-------------------------")

    for key, value in votes_per_candidate.items():
        f.write (f"\n{key} {round((value/votes_cast *100),2)}% ({value})")
    f.write ("\n-------------------------")
    f.write (f"\nWinner: {max(votes_per_candidate,key=votes_per_candidate.get)}")





    
    
