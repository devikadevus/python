start_year=int(input("enter the start year:"))
last_year=int(input("enter the last year:"))
print("feature years are:")
for year in range(start_year,last_year+1):
    if(year % 4 == 0 and year % 100 !=0 or year % 400==0):
        print(year)