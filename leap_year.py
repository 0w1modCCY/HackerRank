import random
def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    else:
        return False


year = 1992
print(year, is_leap(year))
