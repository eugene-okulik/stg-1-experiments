# Эта программа ищет студента по номеру

print("Поиск студента по номеру")
students = {1: "Анна", 2: "Борис", 3: "Виктория"}
student_number = input("Введите номер студента (1-3): ")

student_name = students[student_number]

print("Студент под номером", student_number, ":", student_name)
