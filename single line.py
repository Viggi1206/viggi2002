# Write a program that assigns values to variables for a person's name, age, and favorite color, and prints them in a single line.

#create a function
def persons_detail(value1,value2,value3):
#print the name,age and favorite color
    print("My name is",name,". My age is ",age,". My favorite color is", favorite_color)
#three answers are required
name = input("Enter the name : ")
age = input("Enter the age : ")
favorite_color = input("Enter the favorite color : ")
#Call the function
persons_detail(value1 = name,value2 = age,value3 = favorite_color)
