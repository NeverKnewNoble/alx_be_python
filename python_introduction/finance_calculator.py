# declarations
annual_int_rate = 0.05;

# Input for users
monthly_income = int(input("Enter your monthly income: ")); 
monthly_expenses = int(input("Enter your total monthly expenses: "));

# Monthly Savings
monthly_savings = monthly_income - monthly_expenses;
# Annual Savings
Annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_int_rate);

# Output
print(f"Your monthly savings are ${montlhy_savings}");
print(f"Prohject savings after one year, with interest, is: ${Annual_savings}");
