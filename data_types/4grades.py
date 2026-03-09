# Эта программа вычисляет средний балл из списка оценок

print("Вычисление среднего балла")
grades = "5, 4, 3, 5, 2, 4, 5"
grades_list = list(map(int, grades.split(", ")))

total_grades = len(grades_list)
sum_grades = sum(grades_list)

average = sum_grades / total_grades
print("Средний балл:", average)
