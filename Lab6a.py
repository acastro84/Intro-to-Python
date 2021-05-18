# Adds exception handlers to the previous program.  
# Modifies if statements to naturally close while continuing to use
# fucntion definitions and structure. 
# Outputs selections as a log via text file in the same directory. 

#import the module needed for the conversions

import conversionslabs

#Set constraints for the menu:

MILES_TO_KM = 1
FAH_TO_CELSIUS = 2
GAL_TO_LITERS = 3
POUNDS_TO_KG = 4
INCHES_TO_CM =5
QUIT_CHOICE = 0

  


# The main function

def main():
    try:
        choice = 6
        while choice != QUIT_CHOICE:
            count = 0
            while count < 10:
                display_menu()
            #Get the users choice
                choice = int(input('Please select which conversion you would like to use. Enter 0, to quit. '))
            #Perform the selected action
                if choice == QUIT_CHOICE:
                    print('Exiting Program')
                    count = 10
                elif choice == MILES_TO_KM:
                    sixmiles()
                    count = count + 1
                    
                elif choice == FAH_TO_CELSIUS:
                    sixfah()
                    count = count + 1
                    
                elif choice == GAL_TO_LITERS:
                    sixgal()
                    count = count + 1
                    
                elif choice == POUNDS_TO_KG:
                    sixpounds()
                    count = count + 1
                    
                elif choice == INCHES_TO_CM:
                    sixinches()
                    count = count + 1


            else:
                print('That is 10!!  Exiting program')

                                      

            

            #else choice == QUIT_CHOICE:
              #      print('Exiting Program')    
            
            
    except ValueError:
        choice = input('You must pick a number!  Enter 0 to quit. ')
        if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 0:
            choice = input('You must pick a number from the menu, Enter 0 to quit. ')
           # if choice == 0:
              #  print('Exiting Program')
            
        
        
    #except choice == BAD_CHOICE:
     #   choice = input('You must pick a number from the menu; please try again.  Enter 0 to quit. ')
   # except choice != MILES_TO_KM and choice != FAH_TO_CELSIUS and choice != GAL_TO_LITERS and choice != POUNDS_TO_KG and choice != INCHES_TO_CM and choice != QUIT_CHOICE:
     #   choice = input('You must pick a number from the menu; please try again.  Enter 0 to quit. ')   WHY DOESNT THIS WORK!!!!!!!!??????
        

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
        if inches < 0 or inches == str:
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

#sixinches()




            
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
