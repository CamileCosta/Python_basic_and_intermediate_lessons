players = [
    {'name': 'Matthew Stafford', 'position': 'Quarter Back', 'jersey_number': 9,'yards_gained': 61493, 'touchdowns': 389 },
    {'name': 'Dak Prescott', 'position': 'Quarter Back', 'jersey_number': 4,'yards_gained': 33054, 'touchdowns': 226 },
    {'name': 'Sam Darnold', 'position': 'Quarter Back', 'jersey_number': 14,'yards_gained': 17924, 'touchdowns': 109 }
]

print('Players positions:')
positions = [player['position'] for player in players]
print('Positions: ', positions)
print()

print('Updating player statistics')

player_update = 'Matthew Stafford'

for player in players:
    if player['name'] ==  player_update:
        player['yards_gained'] = 72358
        player['touchdowns'] = 389
        print(f"Updated {player["name"]}'s  statistics")
        print(f'New yards gained: {player["yards_gained"]}')
        print(f'New touchdowns: {player["touchdowns"]}')
        break
print()

print('Average Statistics: ')

total_yards = sum(player['yards_gained'] for player in players)
total_touchdowns = sum(player['touchdowns'] for player in players)

average_yards = total_yards / len(players)
average_touchdowns = total_touchdowns / len(players)

print(f"Average yards gained per player: {average_yards:.2f}")
print(f"Average touchdowns per player: {average_touchdowns:.2f}")
print()

print('All Players statistics:')
for player in players:
    print('Name: ', player['name'])
    print('Position: ', player['position'])
    print('Yards gained: ', player['yards_gained'])
    print('Touchdowns: ', player['touchdowns'])
    print()
