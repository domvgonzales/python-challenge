import os
import csv
budget_csv = os.path.join('PyBank','Resources','budget_data.csv')

Total_Months = []
Total = []
Average_Change  = []
Greatest_Increase_In_Profts = []
Greatest_Decrease_In_Profits = []

with open(budget_csv,'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)
    
  for row in csvreader:
    Total_Months.append(row[0])
    Total.append(int(row[1]))
  for i in range(len(Total)-1):
   Average_Change.append(Total[i+1]-Total[i])

max_increase_value = max(Average_Change)
max_decrease_value = min(Average_Change)

max_increase_month = Average_Change.index(max(Average_Change)) + 1
max_decrease_month = Average_Change.index(min(Average_Change)) + 1     
    
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total)}")
print(f"Average Change: {round(sum(Average_Change)/len(Average_Change),2)}")
print(f"Greatest Increase in Profits: {Total_Months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = os.path.join("PyBank",'Resources', "Financial_Analysis_Summary.txt")


with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Total_Months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Total)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(Average_Change)/len(Average_Change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Total_Months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_value))})")



