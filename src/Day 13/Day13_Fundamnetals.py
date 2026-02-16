import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style ="whitegrid")


# Create Dataset
data = {
    "Age": [25, 30, 35, 40, 28, 32, 45, 50, 23, 36, 29, 41],
    "Salary": [30000, 40000, 50000, 65000, 42000, 48000, 80000, 90000, 28000, 52000, 46000, 70000],
    "Experience": [2, 3, 7, 10, 2, 5, 15, 20, 1, 8, 4, 12],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT", "HR", "Finance"],
    "Gender": ["M", "F", "M", "M", "F", "M", "M", "F", "F", "M", "F", "M"]
}

df = pd.DataFrame(data)

# Dataset Inspection
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

plt.figure()
sns.boxplot(x=df["Salary"])
plt.title("salary distribution")
plt.show()  

print("\ndepartment value counts:")
print(df["Department"].value_counts())  

print("\ngender value counts:")
print(df["Gender"].value_counts())

plt.figure()
sns.countplot(x=df["Department"])
plt.title("Department Distribution")    
plt.show()

plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)    
plt.title("Experience vs Salary")
plt.show()  

plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)    
plt.title("Salary Distribution by Gender")
plt.show()

plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)    
plt.title("Salary Distribution by Department")
plt.show()  

corr_matrix=df.corr(numeric_only=True)
print("\nCorrelation matrix:")
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience Distribution")
plt.show()