# Financial Summary Program

# 1. Store the information using user inputs and variables
name = input("Enter your name: ")
starting_balance = float(input("Enter your starting balance ($): "))
money_received = float(input("Enter the amount of money received ($): "))
money_spent = float(input("Enter the amount of money spent ($): "))

# 2. Calculate the remaining balance using an arithmetic expression
remaining_balance = starting_balance + money_received - money_spent

# 3 & 4. Print a readable financial summary with 2 decimal places
print("\n" + "=" * 40)
print(f"{'FINANCIAL SUMMARY':^40}")
print("=" * 40)
print(f"Account Holder:    {name}")
print(f"Starting Balance:  ${starting_balance:.2f}")
print(f"Money Received:    ${money_received:.2f}")
print(f"Money Spent:       ${money_spent:.2f}")
print("-" * 40)
print(f"Remaining Balance: ${remaining_balance:.2f}")