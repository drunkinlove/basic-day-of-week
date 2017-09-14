# The 1st of January, 1950 is a Sunday. I'll use that as a starting point.

def isitLeapYear(year):
    """
    Determines if the year of the inputted date is a leap year.
    """
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return True
    else:
        return False

def calculateLeapDays(date):
    """
    Calculates the number of leap days between 01.01.1950 and the inputted
    date.

    The first cycle checks if the year from the input is a leap year, too. 
    The second cycle removes that year from the counter if the date we're
    calculating the distance to isn't later than February's last day.
    """
    leapyears = 0
    for i in range(1950, int(date[2]) + 1):
        if isitLeapYear(i) == True:
            leapyears += 1
    if isitLeapYear(int(date[2])) == True and int(date[1]) < 3: 
        leapyears -= 1
    return leapyears

def calculateGap(date):
    """
    Calculates the gap between 01.01.1950 and the inputted date.

    First, we add the full years in between the two dates, then we add leap
    days.
    The first conditional adds a full February, the weirdest month, if the month
    from the input is later.
    Then, we calculate the amount of 31-day months and 30-day months. As they
    interchange (not including February) until August, we must use a slightly
    different algorithm after. So I made two algorithms to count days before
    and after August.
    Finally, we add the days from the input, subtracting one because our
    starting day is the 1st, not the 0th.
    """
    amountofdays = 365 * (int(date[2]) - 1950)
    amountofdays +=  calculateLeapDays(date)
    if int(date[1]) >= 3:
        amountofdays += 28
    amountofdays += 31 * (min(int(date[1]), 8) // 2)
    amountofdays += 30 * (abs((min(int(date[1]), 8)) - 2) // 3)
    if int(date[1]) > 8:
        amountofdays += 31 * ((int(date[1]) - 7) // 2)
        amountofdays += 30 * ((int(date[1]) - 8) // 2)
    amountofdays += int(date[0]) - 1    
    return amountofdays

def determineDayofWeek(amountofdays):
    """
    Determines which day of week it will be, based on the calculateGap result.
    """
    if (amountofdays % 7) == 0:
        dayofweek = "Sunday"
    if (amountofdays % 7) == 1:
        dayofweek = "Monday"
    if (amountofdays % 7) == 2:
        dayofweek = "Tuesday"
    if (amountofdays % 7) == 3:
        dayofweek = "Wednesday"
    if (amountofdays % 7) == 4:
        dayofweek = "Thursday"
    if (amountofdays % 7) == 5:
        dayofweek = "Friday"
    if (amountofdays % 7) == 6:
        dayofweek = "Saturday"
    return dayofweek



inputdate = input("To know what day of week a certain day is, input a date "
                "in the following format: DD.MM.YYYY\n")

inputdate = inputdate.split(".")
result = determineDayofWeek(calculateGap(inputdate))

print("\nIt is a %s." % result)
input("\nPress Enter to close the program.")
