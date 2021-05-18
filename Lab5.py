# Continuation of previous labs.  Using a main with functions to implement the choices listed in the conversion. 






#1. Create the main function:
#2. inside the main function, ask for input of the conversions
#   (Validate Inputs)  
#3. If a valid input is entered, pass it to the 
#   corresponding function and then move to the next input.  
#4. If a valid input is entered 3 times.  Close the program and do not ask for any other inputs. 
#5. Create 5 separate functions for the 5 conversions.  Keep the conversions in these functions, 
#   but pass a value to them using the input from the main.  


def main():
    max_tries = int(0)
    sent = int(0)
    mileamt = float(input("Please enter the amount of miles to convert. "))
    sent = 1
    while sent == 1:
        max_tries = max_tries + 1
        if mileamt < 0:
            print('Miles cannot be less than zero.')
            if max_tries <3:
                print((3 - max_tries), "tries remaining.")
                mileamt = float(input("Please enter a new  number. "))
            else:
                sent = 0
        else:
            sent = 0
    else:
        if max_tries == 3 and mileamt < 0:
            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
        else:
            milesToKm(mileamt)
            max_tries = 0
            sent = 1
            tempf = float(input("Please enter the temperature in Fahrenheit. "))
            while sent == 1:
                max_tries = max_tries + 1
                if tempf > 1000:
                    print('Temperature entered cannot be larger than 1000.')
                    if max_tries < 3:
                        print((3 - max_tries), "tries remaining.")
                        tempf = float(input("Please enter a new number. "))
                    else:
                        sent = 0
                else:
                    sent = 0
            else:
                if max_tries == 3 and tempf > 1000:
                    print(' You entered the incorrect value',max_tries, 'times, closing program. ')
                else:
                    max_tries = int(0)
                    sent = 1
                    FahToCel(tempf)
                    galamt = float(input("Please enter the number of gallons to be converted. "))
                    while sent == 1:
                        max_tries = max_tries +1
                        if galamt < 0:
                            print('Entered amount cannot be less than zero.')
                            if max_tries < 3:
                                print((3 - max_tries), "tries remaining.")
                                galamt = float(input("Please enter a new number. "))
                            else:
                                sent = 0
                        else:
                            sent = 0
                    else:
                        if max_tries == 3 and galamt < 0:
                            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
                        else:
                            max_tries = int(0)
                            sent = 1
                            GalToLit(galamt)
                            templbs = float(input("Please enter the number of pounds to convert. "))
                            while sent == 1:
                                max_tries = max_tries + 1
                                if templbs < 0:
                                    print('Entered amount cannot be a negative number.')
                                    if max_tries < 3:
                                        print((3 - max_tries), "tries remaining.")
                                        templbs = float(input("Please enter a new number. "))
                                    else:
                                        sent = 0
                                else:
                                    sent = 0
                    
                            else:
                                if max_tries == 3 and templbs < 0:
                                    print(' You entered the incorrect value',max_tries, 'times, closing program. ')
                                else:
                                    max_tries = int(0)
                                    sent = 1
                                    PoundsToKg(templbs)
                                    tempinch = float(input('Please enter the number of inches you want to convert. '))
                                    while sent == 1:
                                        max_tries = max_tries + 1
                                        if tempinch < 0:
                                            print('Entered amount cannot be a negative number.')
                                            if max_tries < 3:
                                                print((3 - max_tries), "tries remaining.")
                                                tempinch = float(input('Please enter a new number.'))
                                            else:
                                                sent = 0
                                        else:
                                            sent = 0
                                    else:
                                        if max_tries == 3 and tempinch < 0:
                                            print(' You entered the incorrect value',max_tries, 'times, closing program. ')
                                        else:
                                            InchesToCm(tempinch)
	



def milesToKm(miles):
	kiloconvt = int(miles * 1.6)
	print(miles, 'miles is' ,kiloconvt, 'kilometers.')
	
	
def FahToCel(cels):
	celsconvt = ((cels - 32) * (5/9))
	print(cels, "degrees Fahrenheit is " ,format(celsconvt, '.2f'),"degrees celsius.")
	
def GalToLit(liters):
	ltrconvt = (liters*1.39)
	print(liters, "gallons is ",ltrconvt, "liters.")
	
def PoundsToKg(pounds):
	lbsint = (pounds * .45)
	print(pounds, "pounds is ",lbsint, "Kilograms.")
	
def InchesToCm(inches):
	inchconvt = (inches * 2.54)
	print(inches, "inches is",inchconvt, "centimeters.")

main()
