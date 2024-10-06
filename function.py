def employeeinfo(Name, EmpId, age, Sector, Salary, isActive):
    print(f'e_Name={Name}')
    print(f'e_EmpId={EmpId}')
    print(f'e_age={age}')
    print(f'e_Sector={Sector}')
    print(f'e_Salary={Salary}')
    print(f'e_isActive={isActive}')
    return '---employeeinfo'

print('----')
print(f'Employee_1: {employeeinfo("Jacky", 1, 20, "IT", 50000, True)}')
print('---')
print(f'Employee_2: {employeeinfo("Remo", 2, 30, "HR", 45000, True)}')
print('----')


def customerinfo(Name, orderId, age, City, State, price):
    print(f'c_Name={Name}')
    print(f'c_orderId={orderId}')
    print(f'c_age={age}')
    print(f'c_City={City}')
    print(f'c_State={State}')
    print(f'c_price={price}')
    return '---customerinfo'

print('----')
print(f'customer_1: {customerinfo("Rakesh", 1, 20, "Kanpur", "Uttarpradesh", 600)}')
print('---')
print(f'customer_2: {customerinfo("Suresh", 2, 30, "Raipur", "Chattisgarh", 1200)}')
print('----')
