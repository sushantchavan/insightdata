import random

def deal() :
	deck = [1,2,3,4,5,6,7,8,9,10];
	return random.choice(deck);

def count(player) :
	count = 0
	acecount = 0
	isAce = False
	for card in player:
		if(card == 1):
			isAce = True
			acecount+=1
		else:
			count = count + card;			
	if(count <= 10 and isAce == True and acecount == 1):
		count = count + 11
	elif(count <= 10 and isAce == True and acecount > 1):
		count = count + acecount
	elif(count > 10 and isAce == True):
		count = count + acecount

	return count

def showCards(player) :
	for card in player:
		print card

def options():
	print 'What will be your next move? \n'
	choice = raw_input('Press 1 to Hit and 2 to Stand \n\n')
	if(choice == 1 or choice == 2)
		return choice
	else:
		print 'Please provide a valid input, to quit press q'
		q = raw_input(' ')
		if(q == 'q' or 'Q'):
			exit()
		else:
			options()

def bet(user) :
	betValue = raw_input('Please provide your bet value \n')
	if(user < int(betValue)):
		print 'Bet value is greater than your balance, please provide a value less than\n'
		bet(user)
	else:
		return int(betValue)

def flow(choice,dealer,player) :
	response = 0
	if(int(choice) == 1):
		player.append(deal())
		print 'Player cards are'
		showCards(player)
		if(count(player) == 21):
			print 'Blackjack\n'
			response = 1
		elif(count(player) >21):
			print 'Bust\n'
			response = 1
		else:
			response = action(dealer,player)
			return response
	elif(int(choice) == 2):
		response = action(dealer,player)
	return response
		

def action(dealer,player):
	print 'Dealer cards \n'
	response = 0
	showCards(dealer)
	dValue = count(dealer)
	pValue = count(player)
	if(dValue == 21):
		print 'Dealer Blackjack, You loose\n'
		response = -1
	elif(dValue > pValue):
		print 'Dealer Card value more than yours, You loose\n'
		response = -1
	elif(dValue > 21):
		print 'Dealer lost, you win\n'
		response = 1
	elif(dValue <= pValue):
		dealer.append(deal())
		print 'Dealer picked a card\n'
		showCards(dealer)
		dValue = count(dealer)
		if(dValue < 17):
			action(dealer,player)
		elif(dValue > 17 and (dValue > pValue)):
			print 'You lose'
			response = -1
	return response

def play() :
	print 'Welcom to Casino Maroosh !!!\n\n';
	print 'Let the game beign\n';
	print 'You have a total of 100 Chips to being with ! \n'
	begin = raw_input('Press Y to begin or N to exit \n')
	if(begin == 'y' or begin == 'Y'):
		user = 100;
		count = 0
		isAce = False
		while user > 0:
			betValue = bet(user)
			print 'Dealer has dealt the cards \n'
			print 'Dealer Face Up Card \n '
			dealer = [deal(), deal()];
			player = [deal(), deal()];
			print dealer[0]
			print 'Player cards are \n'
			showCards(player)
			choice = options()
			result = flow(choice,dealer,player)
			if(result == 1):
				user = user + betValue
			elif(result == -1):
				user = user - betValue
			print 'Your balance is '
			print user
			betValue = 0
			dealer = []
			player = []
	else:
		exit()

play()	


	



	