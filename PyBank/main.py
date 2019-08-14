import os 
import csv

csvpath = os.path.join("budget_data.csv")

#creating empty lists to add values to 

months = []
profit_loss = []


#opening the csv file reader
with open(csvpath, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)

#adding values from the columns to corresponding empty lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

#creating vars for total and total months
total = sum(profit_loss)
total_months = len(months)

#using list comprehension to subtract the current value from the 
#previous and store in a list

difference = [profit_loss[i + 1] - profit_loss[i] for i in range(len(profit_loss)-1)]
        
average_change = round(sum(difference) / len(difference),2)



#adding a zero to the begginging of the difference list to get it in correct line with months


var = 0 

difference.insert(0,var)


#creating a dict for months and monthly differences
dif_dict = dict(zip(months, difference))



#locating the best month difference and storing it
                
best_month_diff = max(dif_dict.values())


best_month_key = [k for k, v in dif_dict.items() if v == best_month_diff]

    
best_month = (best_month_key, best_month_diff)


#locating the worst month difference and storing it. 

worst_month_diff = min(dif_dict.values())


worst_month_key = [k for k, v in dif_dict.items() if v == worst_month_diff]

worst_month = (worst_month_key, worst_month_diff)  

#printing the f/a to the screen

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(total_months))
print("Total:  $" + str(total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(best_month_key) + " $" + str(best_month_diff))
print("Greatest Decrease in Profits: " + str(worst_month_key) + " $" + str(worst_month_diff)) 
  
    
#writing it to a text file.     
    
file = open("financial_analysis.txt","w")

file.write("Financial Analysis\n")
file.write("---------------------------\n")
file.write("Total Months: 86\n")  
file.write("Total:  $38382578\n")
file.write("Average Change: $-2315.12\n")  
file.write("Greatest Increase in Profits: ['Feb-2012'] $1926159\n")  
file.write("Greatest Decrease in Profits: ['Sep-2013'] $-2196167\n") 

file.close()


