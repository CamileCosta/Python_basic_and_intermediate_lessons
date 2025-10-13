import random

ball = random.randint(1, 9)
question = input('Question: ')

if ball == 1:
  print('Magic 8 Ball: Yes - definitely')
elif ball == 2:
  print('Magic 8 Ball: It is decidly so')
elif ball == 3:
  print('Magic 8 Ball: Without a doubt')
elif ball == 4:
  print('Magic 8 Ball: Reply hazy, try again')
elif ball == 5:
  print('Magic 8 Ball: Ask again later')
elif ball == 6:
  print('Magic 8 Ball: Better not tell you now')
elif ball == 7:
  print('Magic 8 Ball: My sources say no')
elif ball == 8:
  print('Magic 8 Ball: Outlook not so good')
else:
  print('Magic 8 Ball: Very doubtful')