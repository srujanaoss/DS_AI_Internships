raw_logs =["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)

print("ID05" in unique_users)
#print("ID03" in unique_users)
print(unique_users)

print("Length of raw_logs list:", len(raw_logs))
print("Length of unique_users set:", len(unique_users))

duplicates_removed = len(raw_logs) - len(unique_users)
print("Number of duplicates removed:", duplicates_removed)
