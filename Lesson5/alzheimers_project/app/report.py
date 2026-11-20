# Формування текстового звіту
def create_report(average_age, average_bmi, diagnosis_count):
    report = (
        f"Середній вік пацієнтів: {average_age}\n"
        f"Середній BMI пацієнтів: {average_bmi}\n"
        f"Кількість пацієнтів з діагнозом: {diagnosis_count}"
    )
    return report