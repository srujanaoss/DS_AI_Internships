# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Sample housing dataset (you can replace this with your own CSV)
data = {
    'Price': [250000, 300000, 450000, 500000, 550000, 600000, 750000, 800000, 1200000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Bangalore', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

# -----------------------------
# 1. Histogram with KDE for numerical column (Price)
# -----------------------------
plt.figure()
sns.histplot(df['Price'], kde=True)
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# -----------------------------
# 2. Calculate Skewness and Kurtosis
# -----------------------------
price_skewness = skew(df['Price'])
price_kurtosis = kurtosis(df['Price'])

print("Skewness of Price:", price_skewness)
print("Kurtosis of Price:", price_kurtosis)

# -----------------------------
# 3. Count Plot for categorical column (City)
# -----------------------------
plt.figure()
sns.countplot(x='City', data=df)
plt.title('Count of Houses by City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()