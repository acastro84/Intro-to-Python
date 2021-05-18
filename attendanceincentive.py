# Quickly calculates how many days members can miss prior to being
# ineligible for monthly bonuses. 
# At the time, the current employer had a black & white 
# attendance policy, regardless of excused or non-excused absences. 

# This program will calculate how many days you can miss
# before you fall below your attendance percentage requirement.

# Like the previous, this was compiled into an exe file and ran through CMD.  
# The client wouldnt allow the necessary toolkits to create a GUI UI while on the 
# virtual machine.  

#Get the number of days in the month in question.
month_days = int(input('Please enter the number of days in the month of the work period.'))
if month_days > 31 or month_days < 1 :
    month_days = int(input('Please enter an integer between 1 and 31.'))
else:  #Get the day value for todays date.
    day_of_month = int(input('Please enter the day value for todays date:'))
    if day_of_month < 1 or day_of_month > 31:  # Check input
        day_of_month = int(input('PLease enter an integer between 1 and 31. '))
    else:
        day_of_week = int(input('Please select the day of the week using 1-7. 1 is Monday. 7 is Sunday. Press 0 to exit. '))
        if day_of_week < 1 or day_of_week > 7: #check input
            day_of_week = int(input('Please select the day of the week using 1-7. 1 is Monday. 7 is Sunday. Press 0 to exit. '))
        else:
            hours_missed =  float(input('Please enter the number of hours missed. Available in Connies email. :'))
        prime_day_month = (month_days - day_of_month)
        prime_day_week = (5 - day_of_week)
        if prime_day_week < 0:
            prime_day_week = int(prime_day_week * -1)
        print(' There are ', prime_day_month, 'days left in the month.')
        print('There are ', (prime_day_week), 'days left until the weekend.')
       # print('There are ' unpaid_days, 'unpaid days 
            
