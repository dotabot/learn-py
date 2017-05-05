class welcome (object):
	def first_scene (self):
		print "!!!!!!!!!!!!!Welcome to the world of chaos!!!!!!!!!!!!!"
		print "\n"
		print "Well you have got in and there is no way out unless you prove yourself that your worthy to live"
		print "\n"
		print "Be aware even if you loose once. Your life is at stake !"


hi = welcome()
hi.first_scene()

move = raw_input(">>")


class problem (object):
	def second_scene (self):
		print "This is a test!"
		print "\n"
		print "Here we are gonna test your IQ skill"
		print "\n"
		print "Lets see if you will excel"
		print "\n"
		print "Your brother was twice the age as you when you were 6 years old. "
		print "\n"
		print "what would be his age now if you are ageing 40"
		print "\n"
		print "You have three chances"
		
		guess = raw_input(">>" )
		guesses = 0
		 

		while guess != "46" and guesses <=1:
			print "!!!!!BOOM!!!!!!!"
			print "Wrong answer please try again"
           		guesses += 1
           		guess = raw_input(">>")
		

		if guess == "46":
			print "YAY! you were absoluetely correct. How did you do that.... NERD :P "
			
		else: 
			print "!!!!!!!!!!!! SHIT !!!!!!!!!!!!!!!! "
			print "I wish you were a bit smarter"
			print "better luck next time...."
			print "Try again yes or no"
			choice = raw_input(">>")

			if choice == "yes":

				print "Good choice"
				sol.second_scene()
			else:
				print "GOOD BYE"
				exit()

			
sol= problem()
sol.second_scene()

class love (object):
	def third_scene (self):
		print "\n"
		print "\n"
		print "!!!!!!!  Welcome to the next level !!!!!!!!!"
		print "\n"
		print "Here we have another question that you will need to answer properly else you know the consequences."
		print "\n"
		print "Question : You fell in love with a girl from another kingdom. And your brother at the palace came to know about this and plans something dangerous"
		print "\t Your brother BALLA manipulated your god mother SIVAGAMI and asks her to convice the princess with whom you are in love with to marry BALLA "
		print "\t But you werent aware of this situation and you will be called by the god mother to bring the princess as a prisioner back to the kingdom to punish her for her arrogance in rejecting the marriage proposal with BALLA"
		print "\t Your lovable princess would walk with you even in hell but not as a prisoner and asks you to promise to take care of her till death"
		print "\t You will promise her as per her wish and take her back to the kingdom as your great love"
		print "\t In the Assembly of ministers of the kingdom your love Princess will insult your mother SIVAGAMI for asking her to marry BALLA . As she was in love with you she tells your mother that she wants to marry only you. "
		print "\t SIVAGAMI will ask you to decide between the throne to the kingdom or to the marriage with your love Princess"
		print "\t What would you pick. LOVE or KINGS THRONE ?"

		action = raw_input(">>")

		if action == "love":
			print "\n"
			print "\tWonderful that a good mans move."
			print "\tBut unfortunately your brother hails the throne and will again manipulate your god mother that you tried to kill him"
			print "\tSo your god mother decides to kill you and will ask the royal soldier KATTAPPA to kill you"
			print "\tKATTAPPA will refuse but will then be forced to take up the job as he is a slave to the kingdom"
			print "\tYou will be dead "
			print "\tI know a sad story but there is more to find out so go watch BAHUBALI 2"
			print "\tBYE"

		else :
			print "\n"
			print "\tI know you feel like this is a bad move."
			print "\tBut i gotta say that this would have been the best decision at that time cuz you would get back your love when you kill BALLA for his crooked mind"
			print "\tChill anyways i have nothing to say more just go watch BAHUBALI 2"

bahubali = love()
bahubali.third_scene()



