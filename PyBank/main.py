#dependencies
import os
import csv

# files to retrieve and output
# path from here \Desktop\python_challenge\PyBank
budget_file = os.path.join("Resources", "budget_data.csv")

# lists to store financial parameters
total_months = 0
total_change = 0
total_net = 0
previous_month_value = 0
current_month_value = 0
change = 0
greatest_increase= 0
greatest_decrease= 0
greatest_increase_date = ""
greatest_decrease_date = ""
average_change = 0

with open(budget_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        # read header row before reading the data
        header = next(reader)
        for row in reader:
            # Add up all the profit/loss in the second column
            current_month_value= int(row[1])
            total_net += current_month_value
            total_months +=1
            
            if previous_month_value == 0:
                previous_month_value = current_month_value
            else:
                change = current_month_value - previous_month_value
                previous_month_value = current_month_value
                total_change += change
                if change > greatest_increase:
                    greatest_increase_date = row[0]
                    greatest_increase = change
                elif change < greatest_decrease:
                    greatest_decrease_date = row [0]
                    greatest_decrease = change
            
        average_change = total_change/(total_months-1)
        
 #  format and print the pretty results
text = (f" \n"
f" Financial Analysis \n"
f"  \n"
f"---------------------------------  \n"
f"  \n"
f" Total Months: {total_months} \n"
f"  \n"
f" Total: ${total_net} \n"
f"  \n"
f" Average Change: ${average_change:.2f} \n"
f"  \n"
f" Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase} \n"
f"  \n"
f" Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease} \n"
f"  \n")

print(text)

#Export 
output_file = os.path.join("Analysis","bank_output.txt")
with open(output_file,"w") as txt_file:
    txt_file.write(text)
        
        
   