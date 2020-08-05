import os
import csv

budgetData = os.path.join("Resources/budget_data.csv")
print(budgetData)

with open(budgetData) as csvFile:
    reader = csv.reader(csvFile)
#print(reader)
    for row in reader:
        print(row)

#TotalMonths = 0

#for row in reader:
    #totalMonths = totalMonths + 1


