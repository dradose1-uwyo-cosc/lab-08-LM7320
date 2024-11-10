# Luke Jackson
# UWYO COSC 1010
# Submission Date 11/10/24
# Lab 08
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def stringConverter(answer):
    if "." in answer:
        answer = float(answer)
    elif "." not in answer:
        answer = int(answer)
    return answer
   


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x1, x2):
    y_list = []
    for x in range(x1, x2):
        y = m*x+b
        y_list.append(y)
    return y_list
while True:
    answer_m = input("exit to exit \n Give a number: ")
    answer_b = input("exit to exit \n Give another number: ")
    answer_al = input("exit to exit \n Give a lower bound number: ")
    answer_au = input("exit to exit \n Give a upper bound number: ")

    if "exit" in answer_m.lower():
        break
    else:
        M = stringConverter(answer_m)

    if "exit" in answer_b.lower():
        break
    else:
        B = stringConverter(answer_b)

    if "exit" in answer_al.lower():
        break
    else:
        AL = stringConverter(answer_al)

    if "exit" in answer_au.lower():
        break
    else:
        AU = stringConverter(answer_au)
    
    yl = slope_intercept(M, B, AL, AU)
    print(f"Y value list = {yl}")
    continue


    


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square(a, b, c):
    if b < 0 or c < 0:
        x = ((a**2) - (4*b*c))**0.5
        return x
    


def quadratic(a, b, c):
    value = []
    x1 = (-b+c)/(2*a)
    value.append(x1)
    x2 = (-b-c)/(2*a)
    value.append(x2)
    return value


    
print("Now doing quadratic \n  ")
while True:
    answer_a = input("exit to exit \n Give a number: ")
    answer_b1 = input("exit to exit \n Give another number: ")
    answer_c = input("exit to exit \n Give a negative number: ")
    if answer_a.lower() == "exit":
        break
    else:
        A = stringConverter(answer_a)
    if answer_b1.lower() == "exit":
        break
    else:
        B1 = stringConverter(answer_b1)
    if answer_c.lower() == "exit":
        break
    else:
        C = stringConverter(answer_c)
    
    val = quadratic(A, B1, square(A, B1, C))
    print(f"The quadritc formula answer = {val}")
    continue