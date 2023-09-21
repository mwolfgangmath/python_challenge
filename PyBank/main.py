#dependencies
import os
import csv

# files to retrieve and output
budget_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis","budget_analysis.csv")

# lists to store financial parameters
total_months = 0
net_change = []
#greatest_increase =["",0]
#greatest_decrease = ["", 9999999999]
total_net = 0
greatest_increase=0
greates

with open(budget_file) as csvfile:
        reader = csv.reader(csvfile)
        
        # read header row before reading the data
        header = next(reader)
        first_row = next(reader)
        
        total_months += 1
        
   #JUST TESTING that input file is correct!
        print(f"Header: {header}")
        
print("")
print("Financial Analysis")
print("")
print(f"Total Months: {total_months}")
print("")
print (f"Total: {total_net}")
print("")
print(f"Average Change: {AvgChange}")

        
     
        
     
#with open(output_file."w", newline ='') as datafile:
        #writer=csv.writer(datafile)
        
        #write the header row
        #writer.writerow(["month "," "," "])
            
#cleaned_csv = list(zip(month, profit, change_profit))
        #writer.writerows(cleaned_csv)
