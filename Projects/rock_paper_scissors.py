import random

print('=' * 20)
print('Rock Paper Scissors')
print('=' * 20)

print('1) ✊')
print('2) ✋')
print('3) ✌️')
player = int(input('Pick a number: '))

computer = random.randint(1, 3)

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

