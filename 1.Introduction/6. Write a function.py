def leap_year(year):
    leap = False
    if year%400 == 0:
        leap = True
    else:
        if year%100 == 0:
            leap = False
        else:
            if year%4 == 0:
                leap = True
            else:
                leap = False
    return leap

year = int(input())
print(leap_year(year))