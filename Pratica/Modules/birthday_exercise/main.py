import datetime, birthday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 1, 10)

days_away = next_birthday - today

if today == next_birthday:
    print(birthday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')