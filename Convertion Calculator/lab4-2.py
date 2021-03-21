
test = int(input("Pick '0' for MPG to liters/100km or '1' for liters/100km to MPG"))

number = 282.481

if (test == 0):
    test2 = int(input("How many Miles per Gallon used?"))
    convertMpg0 = number / test2
    print test2, "MPG is", convertMpg0, "L/100km"
elif (test == 1):
    test2 = int(input("How many Liters per 100km used?"))
    convertLiters1 = number / test2
    print test2, "L/100km is", convertLiters1, "MPG"
else: print "INVALED INFOMATION"
