import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader =  next(csvreader)

 # Total Months and Total Profit/Losses

    totalmonths = 0
    months = []
    profitloss = []

    for row in csvreader:
        totalmonths += 1
        profitloss.append(int(row[1]))
        months.append(row[0])

# average of changes
    avechange =[]
    
    for i in range(totalmonths - 1):
        avechange.append(profitloss[i+1]-profitloss[i])

        average = sum(avechange) / len(avechange)

    greatinc = max(avechange)
    greatdec = min(avechange)
    
    for i in range(totalmonths - 1):
        if profitloss[i+1]-profitloss[i] == greatinc:
            greatincmonth = months[i+1]
        if profitloss[i+1]-profitloss[i] == greatdec:
            greatdecmonth = months[i+1]

    print("")    
    print("")    
    print("Financial Analysis:")
    print("-------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${sum(profitloss)}")
    print(f"Average Change: $ {round(average,2)}")
    print(f"Greatest Increase in Profit: {greatincmonth} (${greatinc})")
    print(f"Greatest Decrease in Profit: {greatdecmonth} (${greatdec})")

output_path = os.path.join("..", "PyBank", "PyBank.txt")

with open(output_path, 'w') as txtfile:
    
    txtfile.write("Financial Analysis:\n")
    txtfile.write("-------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${sum(profitloss)}\n")
    txtfile.write(f"Average Change: $ {round(average,2)}\n")
    txtfile.write(f"Greatest Increase in Profit: {greatincmonth} (${greatinc})\n")
    txtfile.write(f"Greatest Decrease in Profit: {greatdecmonth} (${greatdec})\n")