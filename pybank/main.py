import os
import csv

budget_data_csv = os.path.join("budget_data.csv")

month_count = 0
net = 0
revenue_change = 0

with open(budget_data_csv) as f:
    reader = csv.reader(f)
    row = next(reader, None)
    revenue = 0
    high_month = row[0]
    low_month = row[0]
    high_change = revenue
    low_change = revenue
    previous_rev = 0
    sum_change = 0
    revenue_total = 0

    for row in reader:

        month_count = month_count + 1

        revenue = float(row[1])
        net += int(revenue)

        revenue_change = revenue - previous_rev
        sum_change += revenue_change
        previous_rev = revenue

        if revenue_change > high_change:
            high_month = row[0]
            high_change = revenue_change

        if revenue_change < low_change:
            low_month = row[0]
            low_change = revenue_change

average_change = round(sum_change / month_count, 2)

print("Here is the financial analysis: ")
print("--------------------------------")
print(f"Total months: {month_count} months")
print(f"Net total: ${net}")
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: {high_month} ${high_change}")
print(f"Greatest decrease in profits: {low_month} ${low_change}")

write_file = f"pybank_results.txt"
filewriter = open(write_file, mode = 'w')
filewriter.write(f"Financial Analysis for PyBank:\n")
filewriter.write("--------------------------------------------\n")
filewriter.write((f"Total months: {month_count} months\n"))
filewriter.write((f"Net total: ${net}\n"))
filewriter.write((f"Average change: ${average_change}\n"))
filewriter.write((f"Greatest increase in profits: {high_month} ${high_change}\n"))
filewriter.write((f"Greatest decrease in profits: {low_month} ${low_change}\n"))

filewriter.close()
