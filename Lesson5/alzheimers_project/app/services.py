import pandas as pd

from .exceptions import InvalidAgeError

# Перевірка віку пацієнтів
def check_age(ages):
    for age in ages:
        if age < 60 or age > 90:
            raise InvalidAgeError("Вік має бути в межах від 60 до 90 років")
    return True

# Перевірка коректності BMI
def check_bmi(bmi):
    bmi = pd.to_numeric(bmi, errors="coerce")
    invalid_bmi = bmi.isna()
    return invalid_bmi.sum()

# Перевірка перетворення BMI на число
def validate_bmi(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Розрахунок середнього віку пацієнтів
def avg_age(age):
    valid_age = age[(age >= 60) & (age <= 90)]
    return valid_age.mean()

# Розрахунок середнього BMI пацієнтів
def avg_bmi(bmi):
    bmi = pd.to_numeric(bmi, errors="coerce")
    return bmi.mean()

# Кількість пацієнтів з діагнозом "Alzheimer's Disease"
def count_diagnosis(diagnosis):
    return diagnosis.eq(1).sum()

