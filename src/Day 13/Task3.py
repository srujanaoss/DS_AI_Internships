# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (replace with your real dataset)
data = {
    'Price': [250000, 300000, 450000, 500000, 550000, 600000, 750000, 800000, 1200000],
    'SquareFootage': [600, 700, 900, 1000, 1100, 1200, 1500, 1600, 2500],
    'Bedrooms': [1, 2, 2, 3, 3, 3, 4, 4, 5],
    'Bathrooms': [1, 1, 2, 2, 2, 3, 3, 3, 4]
}

df = pd.DataFrame(data)

# ----------------------------------
# 1. Correlation Matrix + Heatmap
# ----------------------------------
corr_matrix = df.corr()

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# ----------------------------------
# 2. Identify highly correlated variables (> 0.8)
# ----------------------------------
high_corr = corr_matrix[(corr_matrix > 0.8) & (corr_matrix < 1.0)]
print("Highly correlated variables (correlation > 0.8):")
print(high_corr)

# ----------------------------------
# 3. Boxplot to detect outliers in main numerical column (Price)
# ----------------------------------
plt.figure()
sns.boxplot(y=df['Price'])
plt.title('Boxplot for Price (Outlier Detection)')
plt.ylabel('Price')
plt.show()