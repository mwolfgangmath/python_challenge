#dependencies
import os
import csv

# files to retrieve and output
BUDGET_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis","bank_output.txt")


# lists to store financial parameters
total_months = 0
total_change = 0
total_net = 0
previous_month_value = None
current_month_value = 0
change = 0
greatest_increase= 0
greatest_decrease= 0
greatest_increase_date = ""
greatest_decrease_date = ""
average_change = 0
print("before", os.getcwd())
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print("after", os.getcwd())
with open(BUDGET_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        # read header row before reading the data
        header = next(reader)
        for row in reader:
            # Add up all the profit/loss in the second column
            current_month_value= int(row[1])
            total_net += current_month_value
            total_months +=1
            
            if previous_month_value is not None:
                change = current_month_value - previous_month_value
        
                total_change += change
                if change > greatest_increase:
                    greatest_increase_date = row[0]
                    greatest_increase = change
                elif change < greatest_decrease:
                    greatest_decrease_date = row [0]
                    greatest_decrease = change
            # prepare for next month row
            previous_month_value = current_month_value
        average_change = total_change/(total_months-1)
        
 #  format and print the pretty results
text = (" \n"
f" Financial Analysis \n"
"  \n"
"---------------------------------  \n"
"  \n"
f" Total Months: {total_months} \n"
"  \n"
f" Total: ${total_net} \n"
"  \n"
" Average Change: ${average_change:.2f} \n"
"  \n"
f" Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase} \n"
"  \n"
f" Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease} \n"
"  \n")

print(text)

#Export 
with open(OUTPUT_PATH,"w") as txt_file:
    txt_file.write(text)
        
        
   