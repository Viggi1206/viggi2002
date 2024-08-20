# Write the Python funtion to check odd or add.

# Create the funtion and use 'def'
def to_check_odd_or_even(number):
# Check the 'nested if' condition
    if (0 < number <= 1000):
        if (0 < number <= 500):
            if number % 2 != 0:
                print(number,"is a Odd number.")
            else:
                print(number,"is not a Odd number.")
        else:
            if number % 2 == 0:
                print(number,"is a Even number.")
            else:
                print(number,"is not a Even number.")
    else:
        print(number,"Please enter the number above 0 to below 1000.")
# one answer are required        
user_number = int(input("Enter the number: ")) 
# Call the funtion
to_check_odd_or_even(number = user_number)
