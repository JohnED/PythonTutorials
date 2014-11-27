#Import function argv from module sys
from sys import argv

#The arguments = the script name and the file name set out in the Powershell command
script, input_file = argv

#Defines function print_all and assigns a variable f which is a file object
def print_all(f):
    print f.read() #prints the content of the file object f
	
def rewind(f):
    f.seek(0)

	
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)