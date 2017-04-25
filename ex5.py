my_name = 'bharath'
my_age = 22 
my_height = 165 # cm
my_weight = 97 # kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name # %s - string
print "He's %d cms tall." % my_height # %d - double
print "He's %d kgs heavy." % my_weight
print "Actually that's heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)