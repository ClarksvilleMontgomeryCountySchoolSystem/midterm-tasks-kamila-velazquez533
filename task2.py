allowance += dishes
allowance += lawn
allowance -= laundry

# Week 2: Bonus week and purchase
allowance += 5
allowance += snack
allowance -= game

 # Week 3: Savings
allowance /= 2

# Print final allowance
print(f'Allowance: ${allowance}')
