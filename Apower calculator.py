from math import*

num1 = input("Animal: ")
num2 = input("Animal weight in lbs: ")
result = pow(float(num2) / 1700, 0.75)
result2 = 1 / pow(float(num2) / 1700, 0.75)
print( "1 " + (num1) + "power = " + str(result) + " Horsepower" )
print( "1 Horsepower = " + str(result2) + " " + (num1) + "power")
