employee_salary=float(input('employee salary :'))
Insurance=(6 * employee_salary)/100
# بیمه
taxes=(4 * employee_salary)/100
# مالیات
Salary_deficit=Insurance+taxes
# جمع کسری بیمه
Salary_received=employee_salary - Salary_deficit
print('Salary received :' , Salary_received)