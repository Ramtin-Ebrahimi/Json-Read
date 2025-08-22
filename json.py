import json


with open(".py/employee.json","r") as employee:
    obj = json.load(employee)

    print("Names and family names of female employees in all companies : \n")
    for Employees_woman in obj:
        if Employees_woman["gender"] == "female":
            print(f'FullName : {Employees_woman["fullName"]}')

    print(10*"**")

    print("Names and family names of male employees of MAPNA company : \n")  
    for Employees_mapna_man in obj:      
        if Employees_mapna_man["gender"] == "male" and Employees_mapna_man["company"] == "MAPNA":
            print(f'FullName : {Employees_mapna_man["fullName"]}')

    print(10*"**")

    print("Names and surnames and emails of employees of Iran Khodro Co. : \n")
    for Employees_Iran_Khodro_co in obj:      
        if Employees_Iran_Khodro_co["company"] == "Iran Khodro Co.":
            print(f'FullName : {Employees_Iran_Khodro_co["fullName"]}\t\tEmail : {Employees_Iran_Khodro_co["email"]}')

    print(10*"**")

    print("Full information of the first three people in terms of salary : \n")
    sorted_employees = sorted(obj, key=lambda x: x['salary'], reverse=True)
    for sorted_employees1 in range(3):
        Employees_salary2 = sorted_employees[sorted_employees1]
        print(f'FullName : {Employees_salary2["fullName"]}\nGender : {Employees_salary2["gender"]}company : {Employees_salary2["company"]}\nSalary : {Employees_salary2["salary"]}\nEmail : {Employees_salary2["email"]}\n',12*"**")