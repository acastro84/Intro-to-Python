#create a function that:
#sets a sentinel
#sets max_tries
#does input validation for value
#uses sentinel to close max_tries and validation.
#returns input
import conversionslabs


# Incomplete.  

def sixmiles():
    sent = 1
    max_tries = 0
    miles = float(input('Please enter the amount of miles. '))
    while sent == 1:
        max_tries = max_tries + 1
        if miles < 0:
            print('Miles cannot be less than zero.')
            if max_tries <3:
                print((3 - max_tries), "tries remaining.")
                miles = float(input("Please enter a new  number. "))
            else:
                sent = 0
                
        else:
            sent = 0

    else:
        if miles < 0 and max_tries == 3:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
        else:
            print(miles, 'miles is' ,conversionslabs.milesToKm(miles), 'kilometers.')
            outfile = open('conversions.txt', 'a')
            outfile.write(str(miles))
            outfile.write(' miles ')
            outfile.write(str(conversionslabs.milesToKm(miles)))
            outfile.write(' kilometers.')
            outfile.close()
#sixmiles()



def sixfah():
    sent = 1
    max_tries = 0
    cels = float(input('Please enter the degrees in Fahrenheit. '))
    while sent == 1:
        max_tries = max_tries + 1
        if cels > 1000:
            print('Temperature entered cannot be larger than 1000.')
            if max_tries < 3:
                print((3 - max_tries), "tries remaining.")
                cels = float(input("Please enter a new number. "))
            else:
                sent = 0
        else:
            sent = 0
    else:
        if max_tries == 3 and cels > 1000:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
            choice = 0
        else:
            print(cels, "degrees Fahrenheit is " ,format(conversionslabs.FahToCel(cels), '.2f'),"degrees celsius.")
            outfile = open('conversions.txt', 'a')
            outfile.write(str(cels))
            outfile.write("  Fahrenheit ")
            outfile.write(str(format(conversionslabs.FahToCel(cels), '.2f')))
            outfile.write(" celsius.")
            outfile.close()

#sixfah()


def sixgal():
    max_tries = 0
    sent = 1
    liters = float(input('Please enter the number of liters to be converted. '))
    while sent == 1:
        max_tries = max_tries +1
        if liters < 0:
            print('Entered amount cannot be less than zero.')
            if max_tries < 3:
                print((3 - max_tries), "tries remaining.")
                liters = float(input("Please enter a new number. "))
            else:
                sent = 0
        else:
            sent = 0
    else:
        if max_tries == 3 and liters < 0:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
            choice = 0
        else:
            print(liters, "gallons is ",conversionslabs.GalToLit(liters), "liters.")
            outfile = open('conversions.txt', 'a')
            outfile.write(str(liters))
            outfile.write( " gallons ")
            outfile.write(str(conversionslabs.GalToLit(liters)))
            outfile.write(" liters.")
            outfile.close()

#sixgal()


def sixpounds():
    max_tries = 0
    sent = 1
    pounds = float(input('Please enter the amount of pounds to be converted. '))
    while sent == 1:
        max_tries = max_tries + 1
        if pounds < 0:
            print('Entered amount cannot be a negative number.')
            if max_tries < 3:
                print((3 - max_tries), "tries remaining.")
                pounds = float(input("Please enter a new number. "))
            else:
                sent = 0
        else:
            sent = 0
        
    else:
        if max_tries == 3 and pounds < 0:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
            choice = 0
        else:
            print(pounds, "pounds is ",conversionslabs.PoundsToKg(pounds), "Kilograms.")
            outfile = open('conversions.txt', 'a')
            outfile.write(str(pounds))
            outfile.write(" pounds ")
            outfile.write(str(conversionslabs.PoundsToKg(pounds)))
            outfile.write(" Kilograms.")
            outfile.close()
#sixpounds()


def sixinches():
    max_tries = 0
    sent = 1
    inches = float(input('Please enter the number of inches to be converted. '))
    while sent == 1:
        max_tries = max_tries + 1
        if inches < 0:
            print('Entered amount cannot be a negative number.')
            if max_tries < 3:
                print((3 - max_tries), "tries remaining.")
                inches = float(input('Please enter a new number.'))
            else:
                sent = 0
        else:
            sent = 0
    else:
        if max_tries == 3 and inches < 0:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
            choice = 0
        else:
            print(inches, "inches is",conversionslabs.InchesToCm(inches),"centimeters.")
            outfile = open('conversions.txt', 'a')
            outfile.write(str(inches))
            outfile.write(" inches ")
            outfile.write(str(conversionslabs.InchesToCm(inches)))
            outfile.write(" centimeters.")
            outfile.close()
