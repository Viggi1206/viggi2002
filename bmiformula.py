# Write the python function to check BMI formula.

# Create the function and use 'def'
def body_mass_index(value1,value2):
# Check the BMI formula
    formula = value1 / value2**2
# Check the return statement 
    return formula
#Two anwsers are required 
weight = int(input("Enter the weight : "))
height = int(input("Enter the height : "))
# print and call the function
print(body_mass_index(value1 = weight,value2 = height))
