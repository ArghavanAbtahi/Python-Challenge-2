# PyPoll
import os
import csv

# reading file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader =  next(csvreader)

    numbervotes = 0
    
    candlist = []
    candict = {}
    voteperc = {}

    # total number of votes casted
    for row in csvreader:
        numbervotes += 1   

        # adding to dictionaries and counting each vote
        if row[2] not in candlist:
            candlist.append(row[2])
            candict[row[2]] = 1
        elif row[2] in candlist:
            candict[row[2]] += 1

    for key, value in candict.items():
        voteperc[key] = str(round((value / numbervotes)*100 , 3)) + "% (" + str(value) + ")"
    
    # finding winner
    winner = max(voteperc.values())
    
    # printing results
    print("Election Results")
    print("-----------------")
    print(f"Total Votes: {numbervotes}")
    print("-----------------")
    for key, value in voteperc.items():
        print(key, value)
    print("-----------------")
    for key, value in voteperc.items():
        if winner == value:
            print(f"Winner: {key}")
    print("-----------------")

    
    # exporting to txt file
    output_path = os.path.join("..", "PyPoll", "PyPoll.txt")
    

    with open(output_path, 'w') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-----------------\n")
        txtfile.write(f"Total Votes: {numbervotes}\n")
        txtfile.write("-----------------\n")
        for key, value in voteperc.items():
            txtfile.write( '%s:%s\n' % (key, value))
        txtfile.write("-----------------\n")
        txtfile.write("Winner: ")
        for key, value in voteperc.items():
            if winner == value:
                txtfile.write( '%s\n' % (key))
        txtfile.write("-----------------")