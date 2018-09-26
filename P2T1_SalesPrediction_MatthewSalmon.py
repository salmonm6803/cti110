# Calculate the profit of the total projected sales.
# September 26 2018
# CTI-110 P2T1 - Sales Prediction
# Matthew Salmon
#

# Get the projected total sales
total_sales = float(input("Enter the projected sales: "))

# Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

# Display the profit
print("The profit of the total projected sales is $", format(profit, ",.2f"))
