import csv
import os

current_dir = os.getcwd()
file_path_top = current_dir.split('python-challenge')[0]



# Establishing the file path for the source data.
file_path = file_path_top + "python-challenge\\PyBank\\budget_data.csv"



# Defining variables to be used later in the script.
total_months = 0
total_revenue = 0
monthly_revenue = []
month_year = []



# Reads the csv and establishes the variable csvreader. Read on a comma delimiter. 
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    #Calculates the variables listed at the begginning of the script. Will be used later in the script. 
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        monthly_revenue.append(int(row[1]))
        month_year.append(row[0])



# Calculates the change in revenue.
revenue_change = [monthly_revenue[i+1]-monthly_revenue[i] for i in range(len(monthly_revenue)-1)]



# Using the variable revenue_change, calculates the average change in revenue. 
average_change = round(sum(revenue_change)/len(revenue_change),2)



# Calculates the greatest increase in profits and lists the month in which it happened. 
greatest_increase = max(revenue_change)
greatest_increase_index = revenue_change.index(greatest_increase)
greatest_increase_month = month_year[greatest_increase_index+1]



# Calculates the greatest decrease in profits and lists the month in which it happened. 
greatest_decrease = min(revenue_change)
greatest_decrease_index = revenue_change.index(greatest_decrease)
greatest_decrease_month = month_year[greatest_decrease_index+1]



# Prints the previously calculated results. 
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${total_revenue}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")



# Export the results to a text file.
with open('output.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_revenue}\n")
    f.write(f"Average Change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")