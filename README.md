# Python-challenge
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)


## General info
 * PyBank
This challenge was for practice on finiancial data within a company. The Result shows the which month had the largest and smallest profit changes
	
* PyPoll
This challenge was for practice on Election Results calculations. The Results proves how many votes total, how much each candidate received and the winner.
	
## Technologies
Project is created with:
* Python 3
* Github
* Visual Basics Code




#import dependencies 
import os
import csv
​
#list of files
row_index = 0
month_counter = 0
sum_revenue = 0
sum_revenue_change = 0
​
revenues = []
months = []
change_revenues = []
​
#   * The total number of months included in the dataset
with open('Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row_index > 0:
            month_counter = month_counter + 1 
​
            month_revenue = int(row[1])
            sum_revenue = sum_revenue + month_revenue
​
            revenues.append(month_revenue)
            
            months.append(row[0])
​
        row_index += 1
​
# Calculate changes in revenues
for i in range(len(revenues) - 1):
    change = revenues[i + 1] - revenues[i]
    change_revenues.append(change)
​
# Calculate the average change
average_change = sum(change_revenues)/len(change_revenues)
​
print("----------------------------------")
​
#   * The greatest increase in profits (date and amount) over the entire period
greatest_increase_profit = max(change_revenues)
month_greatest_increase_profit = change_revenues.index(greatest_increase_profit) + 1
#   * The greatest decrease in losses (date and amount) over the entire period
greatest_decrease_profit = min(change_revenues)
month_greatest_decrease_profit = change_revenues.index(greatest_decrease_profit) + 1
​
print("number of months: ")
print(month_counter)
print("total revenue: ")
print(sum_revenue)
print("average change in revenue: ")
print(average_change)
print("greatest increase in profit: ")
print(greatest_increase_profit)
print("month greatest increase in profit: ")
print(months[month_greatest_increase_profit])
print("greatest decrease in profit: ")
print(greatest_decrease_profit)
print(months[month_greatest_decrease_profit])
​
# Write results to file
with open('results.txt', 'w') as output:
    output.write("number of months: " + str(month_counter))
