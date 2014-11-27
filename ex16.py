from sys import argv

script, filename = argv

print " We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETRUN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

Line1 = raw_input("Line 1: ")
Line2 = raw_input("Line 2: ")
Line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(Line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.write(Line3)
target.write("\n")

print "And finally, we close it."
target.close()

