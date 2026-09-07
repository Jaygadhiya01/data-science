def leap_year(year):
    for i in year:
        if i % 400 == 0:
            print(i,"i is a leap year")
        elif i % 100 == 0:
            print(i," is not a leap year")
        elif i % 4 == 0:
            print(i," is a leap year" )
        else:
            print(i," is not a leap year")
    
leap_year([int(i) for i in input("Enter a year in loop ").split(' ')])




