annual_salary = float(input('Enter the starting salary:​ '))
portion_down_payment = 0.25
annual_return = 0.04
total_cost = 1000000
semi_annual_raise = .07

monthly_salary = starting_salary / 12
down_payment = total_cost * portion_down_payment

current_savings = 0.0
months = 0

while (current_savings * portion_saved) < down_payment:
    if months != 0 and months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

    return_on_investment = current_savings * annual_return / 12
    current_savings += monthly_salary + return_on_investment
    months += 1

print('Number of months:​ ', months)

