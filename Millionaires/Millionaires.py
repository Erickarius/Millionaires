import os
from time import sleep

def Menu():
	print('---------MENU---------\n')
	print('1.Start Game')
	print('2.Player List')
	print('3.Exit\n')
	number = input('Enter a number: ')
	print('\n')
	MenuChoice(number)

def MenuChoice(number):
	if number == '1':
		os.system('cls')
		return Game()
	elif number == '2':
		os.system('cls')
		print('Player List')
		return PlayerList(userName)
	elif number == '3':
		os.system('cls')
		print('Exit')
		input('Press enter to exit')
	else:
		print('There is no such number\n')
		return Menu()

def Game():
	print('Stay a Millionaires!\n')
	print('1. In the UK, the abbreviation NHS stands for National what Service?')
	print('A - Humanity\nB - Health\nC - Honour\nD - Household')
	answer = input('Enter your answer: ')
	if answer == 'B' or answer == 'b':
		pounds = 100
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('2. Which Disney character famously leaves a glass slipper behind at a royal ball')
	print('A - Pocahontas\nB - Sleeping Beauty\nC - Cinderella\nD - Elsa')
	answer = input('Enter your answer: ')
	if answer == 'C' or answer == 'c':
		pounds = 1000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('3. What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?')
	print('A - Hangar\nB - Terminal\nC - Concourse\nD - Carousel')
	answer = input('Enter your answer: ')
	if answer == 'D' or answer == 'd':
		pounds = 10000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('4. Which of these brands was chiefly associated with the manufacture of household locks?')
	print('A - Phillips\nB - Flymo\nC - Chubb\nD - Ronseal')
	answer = input('Enter your answer: ')
	if answer == 'C' or answer == 'c':
		pounds = 50000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('5. The hammer and sickle is one of the most recognisable symbols of which political ideology?')
	print('A - Republicanism\nB - Communism\nC - Conservatism\nD - Liberalism')
	answer = input('Enter your answer: ')
	if answer == 'B' or answer == 'b':
		pounds = 100000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('6. Which toys have been marketed with the phrase \"robots in disguise\"?')
	print('A - Bratz Dolls\nB - Sylvanian Families\nC - Hatchimals\nD - Transformers')
	answer = input('Enter your answer: ')
	if answer == 'D' or answer == 'd':
		pounds = 250000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('7. What does the word loquacious mean?')
	print('A - Angry\nB - Chatty\nC - Beautiful\nD - Shy')
	answer = input('Enter your answer: ')
	if answer == 'B' or answer == 'b':
		pounds = 500000
		print('correct answer, you won %d pounds %s! Let\'s move on to the next question' %(pounds, userName))
		os.system('cls')
		sleep(2)
	else:
		print('Wrong answer, you lose :C')
		sleep(2)
		Menu()

	print('8. Obstetrics is a branch of medicine particularly concerned with what?')
	print('A - Childbirth\nB - Broken bones\nC - Heart conditions\nD - Old age')
	answer = input('Enter your answer: ')
	if answer == 'A' or answer == 'a':
		pounds = 1000000
		print('Congratulations %s, you won a %d pounds! You are Millionaire' %(userName, pounds))
		os.system('cls')
		sleep(2)
		Menu()
	else:
		print('Wrong answer, you lose everything :C')
		sleep(2)
		Menu()


def PlayerList(userName):
	dirPath = os.getcwd()
	filePath = os.path.join(dirPath, 'list.txt')
	fileWrite = open(filePath, 'a')
	fileWrite.write(userName)
	fileWrite.write(' - ')

	fileWrite.write('Pounds\n')
	fileWrite.close()

	fileRead = open(filePath, 'r')
	print(fileRead.read())
	fileRead.close()

	backToMenu = input('Press Enter to return to the menu')
	sleep(2)
	os.system('cls')
	return Menu()
	

userName = input('Enter you are name: ')

os.system('cls')

print('Welcome to Millionaires Game %s!' % userName)

Menu()


