def setup_neutral_buildings(stack):
    for i in range(0,7):
        name = 'Neutral Building ' + str(i + 1)
        current_building = {
            'category': 'neutral',
            'name': name,
            }
        stack.append(current_building)

def setup_player_buildings(stack, color):
    for i in range(0,10):
        name = 'Player Building ' + str(i + 1)
        current_building = {
            'category': 'player',
            'color': color,
            'name': name,
            }
        stack.append(current_building)
