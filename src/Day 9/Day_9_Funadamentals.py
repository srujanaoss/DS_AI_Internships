import pandas as pd 

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)
print("\n")

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])
print("\n")

scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print(passed)
print("\n")

data = pd.Series([15, None, 20, None])

print(data.isnull())
print(data.fillna(0))
print("\n")

names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('A'))
