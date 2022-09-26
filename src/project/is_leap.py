def is_leap(year):
    leap = False
    # Write your logic here
    if year >= 1900:
        print("Number accepted")
        a = year / 4
        b = year /100
        c = year / 400
        if a.is_integer() and c.is_integer():
            leap = True

        return leap

    else:
        exit
  
        
year = int(input())
print(is_leap(year))