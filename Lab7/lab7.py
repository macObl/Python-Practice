
def menu():
    print("1. Test isSorted")
    print("2. Test isAnagram")
    print("3. Test removeDuplicates")
    print("4. Test sumOfSquares")
    print("5. Exit")
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
        exit
    else:
        print("Invalid choice. Please enter 1-5")
        menu()


def test1():
    def isSorted():
        import random

        lst = random.sample(range(3), 3)
        print lst
        even = [0, 1, 2]

        def isSorted(lst):
            if even == lst:
                return True
            return False

        print isSorted(lst)

    isSorted()
    menu()

def test2():
    def isAnagram():
        import random
        import string

        num = "hey"

        def test(num):
            jumble = list(num)
            random.shuffle(jumble)
            print jumble
            print "Rearange the letters in the list to spell the word"
            num2  = str(input("Please use quotation marks around your word"))

            if num == num2:
                return True
            else: return False

        print test(num)

    isAnagram()
    menu()

def test3():
    def removeDuplicates():
        firstList = [1,2,2,3,4]
        secondList = [2,6,2,1,1]

        add = firstList + secondList

        duplicates = list(set(add))

        print "First list of numbers", firstList
        print "Second list of numbers", secondList
        print duplicates

    removeDuplicates()
    menu()

def test4():
    def sumOfSquares():
        print "Enter any number between 1-10"
        num = int(input("First number?"))
        num2 = int(input("Second number?"))
        num3 = int(input("Third number?"))
        num4 = int(input("Forth Number"))
        y = [num, num2, num3, num4]
        print "Your list is", y
        x = [num, num2, num3, num4]
        x[0]= num **2
        x[1] = num2 **2
        x[2]= num3 **2
        x[3]= num4 **2
        print "The squars of your numbers are", x
        z = sum(x)
        print "The sum is", z

    sumOfSquares()
    menu()

menu()
