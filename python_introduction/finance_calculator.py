# Declarations
annual_int_rate = 0.05

# Input for users
monthly_income = int(input("Enter your monthly income: ")) 
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Annual Savings calculation with interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_int_rate)

# Output
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${annual_savings}")
