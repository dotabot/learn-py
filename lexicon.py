class scanner (object):

    def scan (self):

        lexicon = [('direction', 'north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back'),
           ('verb', 'go', 'stop', 'kill', 'eat'),
           ('stop', 'the', 'in', 'of', 'from', 'at', 'it'),
           ('nouns', 'door', 'bear', 'princess', 'cabinet'),
           ('number', '1', '2', '3', '4', '5', '6', '7', '8', '9')]

        enter = raw_input(">>")
        words = enter.split()
        pairs = []

        for word in words:

            if word in lexicon[0]:
                pairs.append(('direction', word))
            elif word in lexicon[1]:
                pairs.append(('verb', word))
            elif word in lexicon[2]:
                pairs.append(('stop', word))
            elif word in lexicon[3]:
                pairs.append(('nouns', word))
            elif word in lexicon[4]:
                pairs.append (('number', word))
            else: 
                pairs.append(('error', word))

        print pairs

sol = scanner()
sol.scan()