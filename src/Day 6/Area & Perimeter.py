def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
#Call the function with user input and print: "Area: X, Perimeter: Y".
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")


