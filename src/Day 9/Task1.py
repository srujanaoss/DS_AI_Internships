import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=["Laptop", "Mouse", "Keyboard"]
)

laptop_price = products.loc["Laptop"]

first_two_products = products.iloc[:2]

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Indexing):")
print(first_two_products)