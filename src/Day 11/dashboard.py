import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)

categories = ['Electronics', 'Clothing', 'Home']
sales =[300, 450, 200]

plt.bar(categories, sales, color=['blue','green','orange'])
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("sales")

# ---- Second Plot: Line Plot ----
plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
months = [1, 2, 3, 4, 5, 6]
trend_values = [250, 300, 350, 420, 480, 510]

plt.plot(months, trend_values, marker='o',  color='red')
plt.title("Sales Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Trend Value")


plt.tight_layout() 

plt.show()