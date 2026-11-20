# Імпорт функцій
from app.data_loader import load_data
from app.services import avg_age, avg_bmi, count_diagnosis, check_age, check_bmi, validate_bmi 
from app.exceptions import InvalidAgeError 
from app.report import create_report 


# Завантаження даних
df = load_data()
if df is None:
    print("Програму зупинено.")
    exit()
print(df)

# Перевірка коректності віку пацієнтів
try:
    check_age(df["Age"])
    print("Всі віки пацієнтів коректні")
except InvalidAgeError as e:
    print(f"Помилка: {e}")

# Перевірка коректності BMI пацієнтів
invalid_bmi_count = check_bmi(df["BMI"])
if invalid_bmi_count > 0:
    print(f"Кількість некоректних значень BMI: {invalid_bmi_count}")
    for value in df["BMI"]:
        if not validate_bmi(value):
            print(f"Некоректне значення BMI: {value}")

# Розрахунок середнього віку пацієнтів
average_age = avg_age(df['Age']).round(0)
print(f"Середній вік пацієнтів: {average_age}")


# Розрахунок середнього BMI пацієнтів
average_bmi = avg_bmi(df['BMI']).round(2)
print(f"Середній BMI пацієнтів: {average_bmi}")


# Кількість пацієнтів з діагнозом
diagnosis_count = count_diagnosis(df['Diagnosis'])
print(f"Кількість пацієнтів з діагнозом 'Alzheimer's Disease': {diagnosis_count}")

# Формування звіту
report = create_report(average_age, average_bmi, diagnosis_count)
print("\nЗвіт:")
print(report)


