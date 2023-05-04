def is_leap():

    year = int(input("please enter the year : "))
    if year % 4 == 0:                   
        if year % 100 == 0 and year % 400 ==0:                    
                print(" {} is a Leap year ".format(year))
        else:
            print(" {} is not a Leap year ".format(year))
    else:
        print(" {} is not a Leap ".format(year))


is_leap()

