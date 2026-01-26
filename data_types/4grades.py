# Эта программа вычисляет средний балл из списка оценок

print("Вычисление среднего балла")
grades = [5, 4, 3, 5, 2, 4, 5]

total_grades = len(grades)
sum_grades = sum(grades)

average = sum_grades / total_grades
print("Средний балл:", average)
