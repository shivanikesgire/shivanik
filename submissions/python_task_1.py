def generate_car_matrix(num_cars):
# Define car attributes
attributes = ["Make", "Model", "Year", "Color"]

# Generate matrix header
matrix = [attributes]

# Generate random data for the matrix
for _ in range(num_cars):
    car_data = [random.choice(["Toyota", "Honda", "Ford", "Chevrolet"]),
                f"Model_{random.randint(1, 10)}",
                random.randint(2000, 2023),
                random.choice(["Red", "Blue", "Green", "Black", "White"])]
    matrix.append(car_data)

return matrix
def print_matrix(matrix):
for row in matrix:
print("|".join(str(cell).ljust(12) for cell in row))
    """
