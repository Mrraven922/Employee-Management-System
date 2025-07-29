def is_valid_age(age):
    return age.isdigit() and 18 <= int(age) <= 65

def is_valid_salary(salary):
    try:
        return float(salary) >= 0
    except:
        return False

