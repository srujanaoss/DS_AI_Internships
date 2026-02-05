contacts = {"Alice": 9741704393, "Bob": 9876543210, "Charlie": 9123456789}
contacts["David"] = 9741704394
print(contacts)
contacts["Alice"] = 9741704395
print(contacts)
print("Alice's number:", contacts.get("Alice"))
print("Eve's number:", contacts.get("Eve", "Contact Not found"))

for name, number in contacts.items():
    print(f"contact:{name} | Phone:{number}")
