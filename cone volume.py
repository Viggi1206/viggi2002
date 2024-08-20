# Find the volume of a cone with radius r and height h. 

# create the function
def calculate_cone_volume(radius, height):
    cone_volume_formula = (1/3)* 3.14 * radius ** 2 * height
# create the return statement
    return cone_volume_formula
# two answers are required for user_height and user_radius
user_height = int(input("Enter the your height value : "))
user_radius = int(input("Enter the your radius value : "))
# print and call the function
print(calculate_cone_volume(radius = user_radius,height = user_height),"is a cone volume value.") check the program
