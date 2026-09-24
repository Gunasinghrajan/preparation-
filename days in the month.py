# Find the number of days in the month of year

year=int(input())
month=int(input())
if month==2 and year%4==0:
    print("29 Days")
elif month==2 and year%4==1:
    print("28 Days")
elif (month==4 or month==6 or month==9 or month==11):
    print("30 Days")
else:
    print("31 Days")
