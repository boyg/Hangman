portion_down_payment = 0.25
r = 0.04 # Annual rate for return on investment

annual_salary = float(input('Enter your annual salary:​ '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home:​ '))
semi_annual_raise = float(input('Enter the semi­-annual raise, as a decimal:​ '))

monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment

current_savings = 0.0
months = 0

while (current_savings * portion_saved) < down_payment:
    if months != 0 and months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

    return_on_investment = current_savings * r / 12
    current_savings += monthly_salary + return_on_investment
    months += 1

print('Number of months:​ ', months)

