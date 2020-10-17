import os
import csv

bank_dict ={}
months = []
income = []
income_delta =0 
income_delta_arr =[]



csvpath = ("Resources/budget_data.csv")

with open (csvpath,'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        months.append(row[0])
        income.append(float(row[1]))
        #bank_dict[row[0]] : row[1]
    
    months_total = len(months)
    income_total = sum(income)
    max_income = income[0]

    for i in range(0, months_total):
        if (income[i] > max_income):
            max_income = income[i]
            max_index = i



#this for-loop calculates the mean delta of each month, we want to start
#at the second month, hence a range starting at 1, and go to the end

    for i in range(1, months_total):
        income_delta = income_delta + (income[i] - income[i-1])
        income_delta_arr.append(income[i]- income[i-1])
    
    delta_pos = income_delta_arr[0]
    delta_neg = income_delta_arr[0]

#Calculate the greatest increase and decrease deltas, and their corresponding month
#index 
    for i in range(0, (months_total-1)):
        if income_delta_arr[i]>delta_pos:
            delta_pos = income_delta_arr[i]
            delta_pos_index = i+1

        if income_delta_arr[i]<delta_neg:
            delta_neg = income_delta_arr[i]
            delta_neg_index = i+1



#since there are 86 months, there will be 85 deltas    
avg_delta = round((income_delta/(months_total-1)),2)

#apply int ops for appearances
delta_pos = int(delta_pos)
delta_neg = int(delta_neg)

print ("Financial Analysis")
print ("-----------------------------------")
print (f"Total Months {months_total}")
print (f"Total: {income_total}")
print (f"Average Change ${avg_delta}")
print (f"Greatest Increase in Profits: {months[delta_pos_index]} ${delta_pos}")
print (f"Greatest Decrease in Profits: {months[delta_neg_index]} ${delta_neg}")

#export to file
f = open ("PyBank_Results.txt", "x")
f.write ("Financial Analysis")
f.write ("\n-----------------------------------")
f.write (f"\nTotal Months {months_total}")
f.write (f"\nTotal: {income_total}")
f.write (f"\nAverage Change ${avg_delta}")
f.write (f"\nGreatest Increase in Profits: {months[delta_pos_index]} ${delta_pos}")
f.write (f"\nGreatest Decrease in Profits: {months[delta_neg_index]} ${delta_neg}")
f.close