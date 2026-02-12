import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned_usernames = usernames.str.strip().str.lower()

contains_a = cleaned_usernames.str.contains('a')

print("Original Usernames:")
print(usernames)

print("\nCleaned Usernames:")
print(cleaned_usernames)

print("\nNames Containing Letter 'a':")
print(contains_a)