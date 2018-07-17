import csv
#Total Vote Counter
total_votes = 0

#candidate options and vote counters
candidate_options = []
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0

#read tghe csv and convert it into a list of dictionaries
with open('election_data.csv') as election_data:
    reader = csv.reader(election_data)

    #read the header
    next(reader)

    #for each row
    for row in reader:
        #print(row)
        #run the loader animation
        #print(", ", end=""),

        #add to the total vote count
        total_votes = total_votes + 1

        #extract the candidate name from each row
        #print(row)
        candidate_name = row(2)

        #print(candidate_name)

                #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add to the list of candidates in the running
            candidate_options.append(candidate_name)
            print(candidate_options)     

        #begin tracking candidates voter count
        candidate_votes[candidate_name] = 0
        print(candidate_votes)  

        #then add vote to candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        print(candidate_votes)
        
