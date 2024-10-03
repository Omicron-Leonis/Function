# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

# Example usage
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")
