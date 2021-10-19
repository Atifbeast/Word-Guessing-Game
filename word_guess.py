import random
import time
from simple_colors import *
word = ['nike','cars','code','oman','oil','land','true','fake','coin']
words = random.choice(word)
dev = ["_"]*len(words)
stack = list(words)
global turns,j,user
turns = 10
j = 11



print(green('         		DESIGNED BY ATIF','bold'))
print(cyan('			    WELCOME','bold'))
print('')
print(red('INSTRUCTION : YOU NEED NOT REPEAT THE WORD WHICH YOU HAVE ALREADY  GUESSED','bold'))
time.sleep(3)
print(yellow('\nYOU HAVE 10 TURNS WITH YOU','bold'))
name = input('\nEnter your name : ')


print(f"\nHi {name} Welcome to the most awaited 'Random Word Guessing' Game")
print('\n')

print(f'The Word is of {len(words)} letters')




# The main software starts
for i in range(turns):
	user = input('\nGuess a letter("A single letter") : ')
	user = user.lower()
	if user in words and user.isalpha():
		value = words.index(user)
		dev[value] = user
		print(f'\ncongratulations {name} you guessed correctly')
		
		print(dev)
		j = j-1
		print(f'You have {j-1} turns with you')
	
	
			
		if dev == stack:
			print(f'\n\nYippee You Nailed it {name}')
			print(f'\nThe Word is {words}')
			exit()
		


		
		
		
	elif user not in words:
		j = j-1
		print(f"You have {j-1} turns with you")
		print(f'Sorry {name} Your word is not in letter')
		
		
		
print(f"\nThe Word was {words}")
	
# The main software ends