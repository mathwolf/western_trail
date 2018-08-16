import tiles

def setup_cattle_card_deck(deck):
        for i in range (0,7):
            current_card = {
                'name': 'Holstein',
                'color': 'yellow',
                'cost': 3,
                'points': 1,
                }
            deck.append(current_card)
        for i in range (0,7):
            current_card = {
                'name': 'Brown Swiss',
                'color': 'red',
                'cost': 3,
                'points': 2,
                }
            deck.append(current_card)
        for i in range (0,7):
            current_card = {
                'name': 'Ayrshire',
                'color': 'blue',
                'cost': 3,
                'points': 3,
                }
            deck.append(current_card)
        # Add brown cards
        for i in range (0,3):
            for j in range (0,3):
                current_card = {
                    'name': 'West Highlands',
                    'color': 'brown',
                    'cost': 4,
                    'points': 3 + i,
                    }
                deck.append(current_card)
        # Add purple cards
        for i in range (0,3):
            for j in range (0,2):
                current_card = {
                    'name': 'Texas Longhorn',
                    'color': 'purple',
                    'cost': 5,
                    'points': 5 + i,
                    }
                deck.append(current_card)

def setup_cattle_market(players, cm, deck):
    maximum = 7 + (players - 2) * 3
    for i in range(0, maximum):
        current_space = tiles.TileSpace()
        current_space.occupant = deck.pop()
        current_space.empty = False
        cm.append(current_space)

def setup_player_cattle_deck(deck, color):
    for i in range(0,5):
        current_card = {
            'name': 'Jersey',
            'color': 'grey',
            'star': color,
            'cost': 1,
            'points': 0,
            }
        deck.append(current_card)
    for i in range(0,3):
        current_card = {
            'name': 'Guernsey',
            'color': 'white',
            'star': color,
            'cost': 2,
            'points': 0,
            }
        deck.append(current_card)
    for i in range(0,3):
        current_card = {
            'name': 'Black Angus',
            'color': 'black',
            'star': color,
            'cost': 2,
            'points': 0,
            }
        deck.append(current_card)
    for i in range(0,3):
        current_card = {
            'name': 'Dutch Belt',
            'color': 'green',
            'star': color,
            'cost': 2,
            'points': 0,
            }
        deck.append(current_card)

def setup_player_hand(deck, hand):
    for i in range (0,4):
        current_space = tiles.TileSpace();
        current_space.occupant = deck.pop()
        current_space.empty = False
        hand.append(current_space)

def setup_objective_deck(deck):
    for i in range (0,24):
        current_card = {
            'name': 'Objective Card ' + str(i + 1),
            'gain': 3,
            'loss': 2,
            }
        deck.append(current_card)

def setup_objective_display(disp, deck):
    for i in range(0, 4):
        current_space = tiles.TileSpace()
        current_space.occupant = deck.pop()
        current_space.empty = False
        disp.append(current_space)

def setup_player_objective_deck(deck):
    for i in range(0,4):
        current_card = {
            'name': 'Objective Card ' + str(i),
            'gain': 3,
            'loss': 0,
            }
        deck.append(current_card)

def setup_player_objective_display(disp, deck):
    current_space = tiles.TileSpace()
    current_space.occupant = deck.pop()
    current_space.empty = False
    disp.append(current_space)
