import random

print('=' * 20)
print('Rock Paper Scissors Lizard Spock')
print('=' * 20)

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
player = int(input('Pick a number: '))

computer = random.randint(1, 5)

if player == 1 and computer == 1:
    print('You chose: ✊')
    print('CPU chose: ✊')
    print("It's a tie!")
elif player == 1 and computer == 2:
    print('You chose: ✊')
    print('CPU chose: ✋')
    print('The CPU won!')
elif player == 1 and computer == 3:
    print('You chose: ✊')
    print('Cpu chose: ✌️')
    print('The player won!')
elif player == 1 and computer == 4:
    print('You chose: ✊')
    print('CPU chose: 🦎')
    print('The CPU won!')
elif player == 1 and computer == 5:
    print('You chose: ✊')
    print('CPU chose: 🖖')
    print('The CPU won!')
elif player == 2 and computer == 1:
    print('You chose: ✋')
    print('CPU chose: ✊')
    print('The player won!')
elif player == 2 and computer == 2:
    print('You chose: ✋')
    print('CPU chose: ✋')
    print("It's a tie!")
elif player == 2 and computer == 3:
    print('You chose: ✋')
    print('CPU chose: ✌️')
    print('The CPU won!')
elif player == 2 and computer == 4:
    print('You chose: ✋')
    print('CPU chose: 🦎')
    print('The CPU won!')
elif player == 2 and computer == 5:
    print('You chose: ✋')
    print('CPU chose: 🖖')
    print('The player won!')
elif player == 3 and computer == 1:
    print('You chose: ✌️')
    print('CPU chose: ✊')
    print('The CPU won!')
elif player == 3 and computer == 2:
    print('You chose: ✌️')
    print('CPU chose: ✋')
    print('The player won!')
elif player == 3 and computer == 3:
    print('You chose: ✌️')
    print('CPU chose: ✌️')
    print("It's a tie!")
elif player == 3 and computer == 4:
    print('You chose: ✌️')
    print('CPU chose: 🦎')
    print('The CPU won!')
elif player == 3 and computer == 5:
    print('You chose: ✌️')
    print('CPU chose: 🖖')
    print('The CPU won!')
elif player == 4 and computer == 1:
    print('You chose: 🦎')
    print('CPU chose: ✊')
    print('The CPU won!')
elif player == 4 and computer == 2:
    print('You chose: 🦎')
    print('CPU chose: ✋')
    print('The player won!')
elif player == 4 and computer == 3:
    print('You chose: 🦎')
    print('CPU chose: ✌️')
    print('The CPU won!')
elif player == 4 and computer == 4:
    print('You chose: 🦎')
    print('CPU chose: 🦎')
    print("It's a tie!")
elif player == 4 and computer == 5:
    print('You chose: 🦎')
    print('CPU chose: 🖖')
    print('The player won!')
elif player == 5 and computer == 1:
    print('You chose: 🖖')
    print('CPU chose: ✊')
    print('The player won!')
elif player == 5 and computer == 2:
    print('You chose: 🖖')
    print('CPU chose: ✋')
    print('The CPU won!')
elif player == 5 and computer == 3:
    print('You chose: 🖖')
    print('CPU chose: ✌️')
    print('The player won!')
elif player == 5 and computer == 4:
    print('You chose: 🖖')
    print('CPU chose: 🦎')
    print('The CPU won!')
elif player == 5 and computer == 5:
    print('You chose: 🖖')
    print('CPU chose: 🖖')
    print("It's a tie!")

