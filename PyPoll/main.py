import os 
import csv


csvpath = os.path.join("election_data.csv")

total_votes_list = []

candidate = []

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

names = []


with open(csvpath, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)

#adding values from the columns to corresponding empty lists
    for row in csvreader:
        total_votes_list.append(row[0])
        candidate.append(row[2])
    

    total_votes = len(total_votes_list) 
    
for x in candidate:
    if x == "Khan":
        khan_votes += 1
    elif x == "Correy":
        correy_votes += 1
    elif x == "Li":
        li_votes += 1
    elif x == "O'Tooley":
        otooley_votes += 1
        khan_p = round((khan_votes/total_votes*100),4)
        correy_p = round((correy_votes/total_votes*100),4)
        li_p = round((li_votes/total_votes*100),4)
        otooley_p = round((otooley_votes/total_votes*100),4)
        
        total_p = [khan_p,
                    correy_p,
                    otooley_p,
                    li_p]
        
        winner_p = max(total_p)
        
    winner = {"name" :"Khan"}
       
    

        
winner         
        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))   
print("-------------------------")
print("Khan: " + str(khan_p) + "% " + "(" + str(khan_votes) + ")")
print("Correy: " + str(correy_p) + "% " + "(" + str(correy_votes) + ")")
print("Li: " + str(li_p) + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_p) + "% " + "(" + str(otooley_votes) + ")")
print("-------------------------")
print("Winner: " + "Khan" )

file = open("results.txt","w")

file.write("Election Results\n")
file.write("---------------------------\n")
file.write("Total Votes: " + str(total_votes) + "\n")  
file.write("-------------------------\n")
file.write("Khan: " + str(khan_p) + "% " + "(" + str(khan_votes) + ")\n")  
file.write("Correy: " + str(correy_p) + "% " + "(" + str(correy_votes) + ")\n")
file.write("Li: " + str(li_p) + "% " + "(" + str(li_votes) + ")\n")
file.write("O'Tooley: " + str(otooley_p) + "% " + "(" + str(otooley_votes) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + "Khan")


file.close()
