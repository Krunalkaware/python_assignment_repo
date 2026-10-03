basic_salary = float(input("Enter basic salary: "))

da = basic_salary * 10 / 100
hra = basic_salary * 20 / 100

gross_salary = basic_salary + da + hra

tax = gross_salary * 5 / 100

net_salary = gross_salary - tax

print("Basic Salary =", basic_salary)
print("DA =", da)
print("HRA =", hra)
print("Gross Salary =", gross_salary)
print("Tax Deduction =", tax)
print("Net Salary =", net_salary)