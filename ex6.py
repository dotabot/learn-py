x = "There are %d types of people." % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

funny = False
evaluation = "Is that joke so funny?! %r"

print evaluation % funny

w = "This is the best part in merging two texts..."
e = "....texts two merging in part best the is this"

print w + e