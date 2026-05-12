#Rule of 72 
# Starting values
savings = 5000
interest_rate = 0.06   # 6%

# Calculations
doubled_balance = savings * 2
years = 72 / (interest_rate * 100)

print("Your current savings is", format(savings, ".2f") + ".")

print(
    "At a",
    format(interest_rate, ".0%"),
    "interest rate, your savings account will be worth",
    format(doubled_balance, ".2f"),
    "in",
    format(years, ".1f"),
    "years"
)