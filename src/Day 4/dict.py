#a = {"name": "Alice", "age": 30}
#print(a["name"])

student = {"name": "Amit", "age": 21, "course": "Engineering"}
print(student["name"])
student["age"] = 22
student["city"] ="Delhi"
print(student)

#To extracting particular value
marks = {"Math": 90, "Science": 85, "English": 88}
print(marks.get("Science"))
print(marks.get("History"))
print(marks.update({"hindi": 92}))
print(marks.pop("Math"))
for subject, score in marks.items():
    print(subject,score)

purchases ={"Alice": 250, "Bob": 400, "Charlie": 150}
for name,amount in purchases.items():
    print(f"{name}: spent ₹{amount}")

    print("Total Customers:", len(purchases))
    print("Customer Names:", purchases.keys())

#Input dictionary from user
n = int(input("Enter number of customers:")) 
user_purchases = {}
for i in range(n):
    name = input("Enter customer name:")
    amount = int(input(f"Enter purchase amount for {name}:"))
    user_purchases[name] = amount
    print("Customer Purchases:", user_purchases)
     
#when we need only the key values
top_customers = max(purchases,key=purchases.get)
print("Highest Spending Customer:", top_customers)

top_customers = min(purchases,key=purchases.get)
print("Lowest Spending Customer:", top_customers)

    