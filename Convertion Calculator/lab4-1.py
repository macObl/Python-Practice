test = int(input("Type which convertion you would like '0' for Fahrenheit to Celsius or '1' for Celsius to Fahrenheit"))

test2 = int(input("Enter in the temperature for convertion"))

convertF = (test2 - 32) * 5 / 9
convertC = (test2 * 9 / 5 ) + 32

if (test == 0):
    print(test2, "Fahrenheit is", convertF, "Celsius")
elif (test == 1):
    print(test2, "Celsius is", convertC, "Fahrenheit")
else: print "Invaled Nubmer"
