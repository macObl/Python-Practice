
def menu():
    print("1. Test Exercise 2")
    print("2. Test myFactorial")
    print("3. Test checkOddEven")
    print("4. Test printAsterisksv1")
    print("5. Test printAsterisksv2")
    print("6. Test printDiagonally")
    print("7. Exit")
    selection = int(input("Please enter in choice: "))
    if selection == 1:
        test1()
    elif selection == 2:
        test2()
    elif selection == 3:
        test3()
    elif selection == 4:
        test4()
    elif selection == 5:
        test5()
    elif selection == 6:
        test6()
    elif selection == 7:
        exit
    else:
        print("Invalid choice. Please enter 1-7")
        menu()


def test1():
    n = int(input("Pick a number between 1-5?"))

    def printTriangularNumbers(n):
        number = 0
        while number != n:
            for x in range(1, n+1):
                print x, x * (x + 1) / 2
            break
        return number

    printTriangularNumbers(n)
    menu()

def test2():
    n = int(input("Pick a number?"))

    def myFactorial(n):
        num = 1
        while n >= 1:
            num = num * n
            n = n -1
            print num
        return num

    myFactorial(n)
    menu()

def test3():
    n = 0
    n1= n + 2
    def checkOddEven(n):
        for x in range(0, 21):
            if (x%2 == n):
                x = x, "even"
            else :
                x = x, "odd"
            print x
        return x

    checkOddEven(n)
    menu()

def test4():
    n = int(input("Number between 1-10?"))

    def printAsterisksv1(n):
        for x in range(0, 11):
            x  = x + n
            print x, "*"
        return x
    printAsterisksv1(n)
    menu()

def test5():
    x = int(input("Number between 1-10?"))

    def printAsterisksv2(x):
        while x in range(0, 11):
            print x, "*"
            x = x +1
        return x
    printAsterisksv2(x)
    menu()

def test6():
    n = raw_input("Type one word.")
    space = " "

    def printDiagonally(n):
        for x in range(len(n)):
            print '' * x, n[x]
        return x

    printDiagonally(n)
    menu()


menu()
