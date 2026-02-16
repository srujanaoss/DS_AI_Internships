# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (replace with your actual dataset)
data = {
    'SquareFootage': [500, 750, 1000, 1250, 1500, 1800, 2200],
    'Price': [250000, 350000, 500000, 650000, 800000, 950000, 1200000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)

# ----------------------------------
# 1. Scatter Plot: SquareFootage vs Price
# ----------------------------------
plt.figure()
sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title('Square Footage vs House Price')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.show()

# ----------------------------------
# 2. Boxplot: City vs Price
# ----------------------------------
plt.figure()
sns.boxplot(x='City', y='Price', data=df)
plt.title('House Price Distribution by City')
plt.xlabel('City')
plt.ylabel('Price')
plt.show()