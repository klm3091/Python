import os

import csv

with open('Budget_Data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    next(csvreader)
    
    #Set variables
    total = 0
    revenue_difference = 0
    previous_revenue = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999]
    revenue_changes = []

    #Calculations
    for row in csvreader:
        print(row)
        row_count = sum(1 for row in csv.reader( open('Budget_Data.csv') ) )
        total += float(row[1])
        revenue_difference = float(row[1]) - previous_revenue
        previous_revenue = float(row[1])

        if (revenue_difference > greatest_increase[1]):
            greatest_increase[1] = revenue_difference
            greatest_increase[0] = row[0]

        if (revenue_difference < greatest_decrease[1]):
            greatest_decrease[1] = revenue_difference
            greatest_decrease[0] = row[0]

        revenue_changes.append(revenue_difference)

#Print findings
print("Financial Analysis")
print("......................................")
print(f"Total Months: {str(row_count)}")
print('Total {}'.format(total))
print("Average Change: " + str(round(sum(revenue_changes) / len(revenue_changes))))
print("Greatest Increase: " + str(greatest_increase[0] + " " + str(greatest_increase[1])))
print("Greatest Decrease: " + str(greatest_decrease[0] + " " + str(greatest_decrease[1])))

with open("Pybank.txt", "w") as text_file:
    text_file.write("Financial Analysis")
    text_file.write("_____________________________________")
    text_file.write(f"Total Months: {str(row_count)}")
    text_file.write('Total {}'.format(total))
    text_file.write("Average Change: " + str(round(sum(revenue_changes) / len(revenue_changes))))
    text_file.write("Greatest Increase: " + str(greatest_increase[0] + " " + str(greatest_increase[1])))
    text_file.write("Greatest Decrease: " + str(greatest_decrease[0] + " " + str(greatest_decrease[1])))

