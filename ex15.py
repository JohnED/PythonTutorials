#This imports a list of arguments
from sys import argv

#The argument is expected to contain 2 variables:
#The name of the script and the name of the file
script, filename = argv

#This assigns the value to the function txt
#The value is an command to open a file as set within its parameters
txt = open(filename)

print "Here's your file %r:" % filename #This prints the name of the file
print txt.read() #This prints the contents of the file

txt.close()

print "Type the file name again:" 

#This assigns the value to the function file_again
#The value is raw input from the user
#The user is shown the prompt >
file_again = raw_input("> ")

#This assigns the value to the function text_again
#The value is an command to open a file as set within its parameters
text_again = open(file_again)

print  text_again.read() #This prints the contents of the file

txt.close()

