#This program tracks grades from students and collects an average.

runtotal =  float(0)
count = int(0)
avg = float(0)
sent = int(0)

#ask the user for the grade

num = int(input('Please enter the first grade.  Enter -1 to stop. '))
sent = 1
while sent == 1:
    if num >= 0:
        if num > 100:
            num = int(input('Invalid grade.  Please try again. '))
        else:
            count = count + 1
            runtotal = num + runtotal
            if num > 90:
                print(' You made an A.  Nice.')
            elif num >= 80 and num < 90:
                print(' You made a B.  You can do better.')
            elif num >= 70 and num < 80:
                print('You made a C. Perhaps you should see a tutor?')
            elif num >= 60 and num < 70:
                print('You made a D. Do you even have the book?')
            elif num < 60:
                print('You made an F!!  You are fired.  Get out!!')
            num = int(input('Please enter the next grade.  Enter -1 to stop. '))
    else:
        sent = 0

    
    
#add the count for the grade
#add the grade to the current running total of grades
#finish the loop with -1
#average the grades unless there are zero grades

avg = runtotal / count
print('The number of grades entered is', count,".")
print('The average of the grades entered is', avg,".")

