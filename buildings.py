import act

def setup_neutral_buildings(stack):
    letter_list = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
    action_list = [
        [],
        [],
        [],
        [],
        [],
        [],
        ['sell_white_2', 'buy_worker']
        ]
    for i in range(0,7):
        name = 'Neutral Building ' + letter_list[i]
        current_building = {
            'category': 'neutral',
            'name': name,
            'action_list': action_list[i]
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
