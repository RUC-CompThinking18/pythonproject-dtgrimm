


#the following code requests an input from a user and assigns the input to a variable
#the user will type what they want inputted and when they press enter it will be printed to the terminal
question = raw_input('Press "Enter" to find out what this program does.:')
#assigns input to a variable so that it can be printed
print 'This is a program that displays the effects of global warming by entering different degrees of warming.'
#prints the data stored in the variable

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "Improved public health"#this is if global warming reduces, showing that we have made progress
elif number > 1.5 and number < 2.0: #this is if global warming becomes worse, showing we haven't made any progress
    print "Spike in flooding"
else: # this if the number is above 2.0, meaning global warming has become near irrerversible
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number) #this converts a string to a float, because, if not, using raw_input for anything other than a string will throw an error
type(number)

if number < 1.5:
    print "Preserves key ecosystems and species"
elif number > 1.5 and number < 2.0:
    print "Water scarcity"
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "Enhanced global and national security"
elif number > 1.5 and number < 2.0:
    print "Longer drought periods"
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "More jobs created."
elif number > 1.5 and number < 2.0:
    print "More frequent extreme rainfall over land."
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "Cleaner water"
elif number > 1.5 and number < 2.0:
    print "Increased chance of species losing over 50% of their climate range"
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "Eased pressure on the Artic"
elif number > 1.5 and number < 2.0:
    print "Completely eradicated corals"
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "Amount of people exposed to water stress drops by 50%"
elif number > 1.5 and number < 2.0:
    print "Amount of people exposed to water stress rises by 50%"
else:
    print "We've failed"

number = raw_input('Enter a number between 1.0C and 2.0C:')
number = float(number)
type(number)

if number < 1.5:
    print "10 million more people effected by rise in sea-levels"
elif number > 1.5 and number < 2.0:
    print "10 million less people effected by rise in sea-levels"
else:
    print "We've failed"
