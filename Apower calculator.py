
animal = input("Animal: ")
aweight = float(input("Animal weight in lbs: "))

result = pow(aweight / 1700, 0.75)
result2 = 1 / pow(aweight / 1700, 0.75)

print("1 " + animal + "power = " + str(result) + " Horsepower")
print("1 Horsepower = " + str(result2) + " " + animal + "power")
