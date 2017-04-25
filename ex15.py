from sys import argv
script, filename = argv
txt= open (filename)
print "Here is your file %r." % filename
print txt.read()

print "retype the file name"
temp= raw_input(">>")
txt_again = open (temp)
print txt_again.read()