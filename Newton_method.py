from sympy import *
import math

def differentiation(expression):
    x, y = symbols('x y')
    
    #print("Before Differentiation : {}".format(gfg_exp))
    
    # Use sympy.diff() method
    dif = diff(expression, x)   
    return str(dif)


function_input=input("Enter Function Expression:")

check_initial=(input("Is there initial value for x (y/n):"))
while check_initial != "y" and check_initial != "n":
    check_initial=(input("Is there initial value for x (y/n):"))
if check_initial=="y":
    x=float(input("Enter the Initial X:"))
elif check_initial=="n":
    x=0

check_iterations=(input("Is there number of iterations(y/n):"))
while check_iterations != "y" and check_iterations != "n":
    check_iterations=(input("Is there number of iterations(y/n):"))
if check_iterations=="y":
    number_of_iterations=int(input("Enter the Number of Iterations:"))
elif check_iterations=="n":
    number_of_iterations=0

check_error=(input("Is there error value(y/n):"))
while check_error != "y" and check_error != "n":
    check_error=(input("Is there error value(y/n):"))
if check_error=="y":
    error=float(input("Enter the Error Value:"))
elif check_error=="n":
    pass


if number_of_iterations!=0:
    for i in range(number_of_iterations):
        if i>0:
            x=next_x
        lower_term=eval(differentiation(function_input))
        while lower_term==0:
            x+=1
            lower_term=eval(differentiation(function_input))
        upper_term=eval(function_input)
        next_x=x-(upper_term/lower_term)
        #print(next_x)

        absolute_error=abs(next_x-x)
        try:
            if absolute_error<error:
                break
            #print(i)
        except:
            pass
else:
    absolute_error=1+error
    i=0
    while absolute_error>error:
        if i>0:
            x=next_x
        lower_term=eval(differentiation(function_input))
        while lower_term==0:
            x+=1
            lower_term=eval(differentiation(function_input))
        upper_term=eval(function_input)
        next_x=x-(upper_term/lower_term)
        try:
            absolute_error=abs(next_x-x)
            if absolute_error<error:
                break
        except:
            pass
        i+=1
print(f"Answer Is:{next_x}")