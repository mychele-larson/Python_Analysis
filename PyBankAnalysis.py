#import modules
import os
import csv

#set path for file
csvpath = os.path.join('..','Resources', 'budget_data.csv')

#set the output of the text file
text_path = "Final_Analysis.txt"

#Set variables
totalmonths = []
profits = []
pc = []

# Method 2 using CVS Module
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile) #, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

for i in range(len(profits) - 1):
        pc.append(profits[i+1] - profits[i])


print(len(totalmonths))
print(sum(profits))
print(sum(pc) / len(pc))
print(totalmonths[pc.index(max(pc))+1])
print(totalmonths[pc.index(min(pc))+1])
print(min(pc))
  
#print(totalmonths.index("Jan-10"))
#write changes to csv
with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % (totalmonths.index("Jan-10")))
        file.write("Total Profits: $%d\n" % (sum(profits)))
        file.write("Average Revenue Change $%d\n" % (sum(pc) / len(pc)))
        file.write("Greatest Increase in Profits: %s ($%s)\n" % (totalmonths[pc.index(max(pc))+1]))
        file.write("Greatest Decrease in Profits: %s ($%s)\n" % ((totalmonths[pc.index(min(pc))+1])))



