filename    = input("Enter the file name: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")        