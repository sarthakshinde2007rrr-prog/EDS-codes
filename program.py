








# Taking input for mass and velocity as floating-point numbers
mass = float(input("Enter mass in kilograms: "))
velocity = float(input("Enter velocity in meters per second: "))

# Calculating momentum using the formula p = m * v
momentum = mass * velocity

# Displaying the result rounded to 2 decimal places with the required units
print(f"{momentum:.2f} kgm/s")
