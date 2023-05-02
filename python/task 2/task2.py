def is_leap():

    year = int(input("please enter the year : "))
    if year % 4 == 0:                   # check if the year can be divided by 4
        if year % 100 == 0:             # check if the year can be divided by 100
            if year % 400 == 0:         # check if the year can be divided by 400
                print(" {} is a Leap year ".format(year))
            else:
                print(" {} is not a Leap year because it can't be evently divided by 400".format(year))
        else:
            print(" {} is not a Leap year because it can't be evently divided by 100".format(year))
    else:
        print(" {} is not a Leap year because it can't be evently divided by 4".format(year))


is_leap()


'''

another way:
def leap_year ():
     year = int(input("please enter a year :"))
     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:   check all conditions in 1 statement
           print("{} is a leap year".format(year))
     else:
           print("{} is not a leap year".format(year))

leap_year()


'''
