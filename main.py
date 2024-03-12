import random

print('Welcome to rock paper and scissor game !')
choices = ['🪨', '📰', '✂️']
user_choice = int(input('Enter 0 for rock, 1 for paper and 2 for scissor : '))
computer_choice = random.randint(0, len(choices) - 1)
print(f'You chose {choices[user_choice]} ')
print(f'Computer chose {choices[computer_choice]}')
if user_choice == computer_choice:
    print('Match Draw')
if user_choice == 0 and computer_choice == 1:
    print('Computer Won. You Lose !')
if user_choice == 0 and computer_choice == 2:
    print('You Won !')
if user_choice == 1 and computer_choice == 0:
    print('You Won')
if user_choice == 1 and computer_choice == 2:
    print('Computer won ! You lose !')
if user_choice == 2 and computer_choice == 0:
    print('Computer Won. you lose !')
if user_choice == 2 and computer_choice == 1:
    print('You Won ')
