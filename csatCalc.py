# I created this to allow customer service agents to calculate their
# own incentive requirements based off of dynamically changing metrics.
# ******************************************************************
# The idea here is if the agent knows their currently scored surveys, 
# they can enter the number of surveys that do not meet bonus criteria, 
# and those that do. Based on the ratio, the program calculates:

# How many surveys they need to meet minimum requirements or how many
# additional surveys would be needed to correct already scored surveys
# that do not meet bonus criteria.  

# How many surveys need to meet criteria to meet minimum percentage for
# a bonus.  This file was used to create a batch.exe that was saved to
# every desktop.  The program also allowed exporting of requested information
# to a .txt file within the same directory.  The line below shows 
# the comments included in the documentation of the script. 

# The number of good csats you need to get == 20% of the percentage of 
# good csats divided by the percentage of the bad csats
#*******************************************************************


# to calculate the good and bad percentage of csats: 
# take the number of good csats and divide it by the total # of csats
# take the number of bad csats and divide it by the total # of csats

# to calculate the number of csats you need to hit you will need the 
# percentage of good csats you need to hit.  Then multiply that number by 
# the good csat percentage divided by the bad csat percentage. 

# To find the percentage of the number of good csats you need to hit 
# in relation to the total number of csats,  

# for example:

# a == number of good csats
# b == number of bad csats
# t == total number of csats (a + b)
# z == the number of good csats you need to hit to qualify for incentive

# a% == (a/t)
# b% == (b/t)
# z == (.2) * (a%/b%)

translated into code:


goodcsats == int(a):
badcsats == int(b):
total == int(a+b):
totalfl == float(int):
goodperc == float(goodcsats/total):
badperc == float(badcsats/total):
numbertohit == float(.2 * (goodcsats/badcsats)):
numbertohiti == int(numbertohit):
relationperc == float(numbertohit/totalfl):
print(relationperc):




goodcsats = int(a)
badcsats = int(b)
total = int(a+b)
totalfl = float(total)
goodperc = float(goodcsats/total)
badperc = float(badcsats/total)
numbertohit = float(.2 * (goodcsats/badcsats))
numbertohiti = int(numbertohit)
relationperc = float(numbertohit/totalfl)



