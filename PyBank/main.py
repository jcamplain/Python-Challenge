import os
import csv
file = os.path.join("Resources/budget_data.csv")
with open(file) as csvfile:
    csvReader = csv.reader(csvfile)
    csvHeader = next(csvReader)
    
    totalMonths = []
    TprofitLosses = []
    changeProfit = []
    
    for row in csvReader:
        totalMonths.append(row[0])
        TprofitLosses.append(int(row[1]))
    for i in range(len(TprofitLosses)-1):
        changeProfit.append(TprofitLosses[i+1]-TprofitLosses[i])
                      
increase = max(changeProfit)
decrease = min(changeProfit)

monthIncrease = changeProfit.index(max(changeProfit))+1
monthDecrease = changeProfit.index(min(changeProfit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(totalMonths)}")
print(f"Total: ${sum(TprofitLosses)}")
print(f"Average Change: {round(sum(changeProfit)/len(changeProfit),2)}")
print(f"Greatest Increase in Profits: {totalMonths[monthIncrease]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {totalMonths[monthDecrease]} (${(str(decrease))})")      

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {len(totalMonths)}")
line4 = str(f"Total: ${sum(TprofitLosses)}")
line5 = str(f"Average Change: {round(sum(changeProfit)/len(changeProfit),2)}")
line6 = str(f"Greatest Increase in Profits: {totalMonths[monthIncrease]} (${(str(increase))})")
line7 = str(f"Greatest Decrease in Profits: {totalMonths[monthDecrease]} (${(str(decrease))})")
#\n to write on a new line
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))