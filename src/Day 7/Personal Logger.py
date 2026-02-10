name=input("Enter your name:")
goal=input("Enter your daily goal:")
with open("journal.txt","a") as file:
     file.write(f"Name: {name}, Goal: {goal}\n")
     print("Data saved successfully!")