salary = float(input())

if 0<salary<=400:
    porcentage = 15
    new_salary = (salary+(salary*0.15))
    upgrade = (new_salary-salary)
    print('New salary = {}'.format(new_salary))
    print('Upgrade salary = {}'.format(upgrade))
    print('Porcentage = 15%')
elif 400.1<=salary<=800:
    porcentage = 12
    new_salary = (salary+(salary*0.12))
    upgrade = (new_salary-salary)
    print('New salary = {}'.format(new_salary))
    print('Upgrade salary = {}'.format(upgrade))
    print('Porcentage = 12%')
elif 800.1<=salary<=1200:
    porcentage = 10
    new_salary = (salary+(salary*0.10))
    upgrade = (new_salary-salary)
    print('New salary = {}'.format(new_salary))
    print('Upgrade salary = {}'.format(upgrade))
    print('Porcentage = 10%')
elif 1200<=salary<=2000:
    porcentage = 7
    new_salary = (salary+(salary*0.07))
    upgrade = (new_salary-salary)
    print('New salary = {}'.format(new_salary))
    print('Upgrade salary = {}'.format(upgrade))
    print('Porcentage = 7%')
else:
    porcentage = 4
    new_salary = (salary+(salary*0.04))
    upgrade = (new_salary-salary)
    print('New salary = {:.2f}'.format(new_salary))
    print('Upgrade salary = {:.2f}'.format(upgrade))
    print('Porcentage = 4%')