grades = []

N = int(input("How many number of test scores? "))

for i in range(N):
    grade = int(input("Enter grade: "))
    grades.append(grade)
    
grades.sort()

maximum = max(grades)
minimum = min(grades)
average = sum(grades) / N

print(f"{grades}\n Maximum grade = {maximum}\n Minimum grade = {minimum}\n Average grade = {average}")