#Cleans up previous code a user menu.  Imports package conversionlabs to perform the conversion functions.  


#import the module needed for the conversions

import conversionslabs

#Set constraints for the menu:

MILES_TO_KM = 1
FAH_TO_CELSIUS = 2
GAL_TO_LITERS = 3
POUNDS_TO_KG = 4
INCHES_TO_CM =5
QUIT_CHOICE = 0
QUIT2 = int(2)


# The main function

def main():
    choice = 6
    while choice != QUIT_CHOICE:
        display_menu()
        #Get the users choice
        choice = int(input('Please select which conversion you would like to use. '))
        #Perform the selected action
        if choice == MILES_TO_KM:
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
                if max_tries == 3 and miles < 0:
                    print(' You entered the incorrect value',max_tries, 'times, closing program. ')
                    choice = 0
                else:
                    print(miles, 'miles is' ,conversionslabs.milesToKm(miles), 'kilometers.')
        elif choice == FAH_TO_CELSIUS:
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
        elif choice == GAL_TO_LITERS:
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
        elif choice == POUNDS_TO_KG:
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
        elif choice == INCHES_TO_CM:
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
                    print(inches, "inches is",conversionslabs.InchesToCm(inches), "centimeters.")
        elif choice == QUIT_CHOICE:
            QUIT2 = 2
    else:
        if choice == 6 and QUIT2 != 2:
            choice= input('Invalid Selection. Please try again. Enter 0 to quit. ')
        else:
            print('Exiting Program. ')
            
# The display function displays a menu for the user
def display_menu():
    print(' Menu' )
    print('1) Miles to Kilometers')
    print('2) Fahrenheit to Celsius')
    print('3) Gallons to Liters')
    print('4) Pounds to Kilograms')
    print('5) Inches to Centimeters')
    print('0) Quit')



# Call the main function
main()
