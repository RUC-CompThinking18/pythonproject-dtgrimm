#the following code requests an input from a user and assigns the input to a variable
#the user will type what they want inputted and when they press enter it will be printed to the terminal
question = raw_input('Enter "What is this?":')
#assigns input to a variable so that it can be printed
print 'This is a program that displays the effects of global warming by entering different degrees of warming.'
#prints the data stored in the variable
number = raw_input('Enter a number between 1.0C and 2.0C:')
if number < 1.5:
    print "Improved public health"
if number > 1.5 and number < 2.0:
    print "Spike in flooding"
else: # this if the number is above 2.0, meaning global warming has become near irrerversible
    print "We've failed"

number = raw_input('Enter another number between 1.5C and 2.0C:')
print 'Increased poverty.'
