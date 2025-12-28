def employee(name):
    print(name)
def salary(exp):
    if exp>=5:
        return 3000000
    elif exp>=3:
        return 100000
    else:
        return 500000
employee("Shreyansh")
a=salary(2)
print("the salary of the emplyee is ",a)