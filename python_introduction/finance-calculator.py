income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = income - expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# Prompt the user for financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

print(f"Your monthly savings are ${monthly_savings}.")
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)


print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")