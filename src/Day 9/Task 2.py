import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()

filled_grades = grades.fillna(0)

filtered_grades = filled_grades[filled_grades > 60]

print("Original Series:")
print(grades)

print("\nMissing Values (True means missing):")
print(missing_values)

print("\nFilled Series (Missing replaced with 0):")
print(filled_grades)

print("\nFiltered Scores (Greater than 60):")
print(filtered_grades)