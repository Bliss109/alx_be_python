# Personal Finance Calculator

# Ask for user input and convert to float for flexibility
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Annual savings with 5% interest
rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")

