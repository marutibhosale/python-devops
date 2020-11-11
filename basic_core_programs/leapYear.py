def checkLeapYear(year):
    if len(str(year)) == 4:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(str(year) + " is Leap year")
        else:
            print(str(year) + " is not Leap year")
    else:
        print("invalid year")
    return


yearValue = int(input("Enter year: "))
checkLeapYear(yearValue)
