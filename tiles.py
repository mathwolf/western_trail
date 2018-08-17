class TileSpace(object):
    def __init__(self):
        '''
        empty:      <bool>
        occupant:   <obj> card or tile currently contained in space
        '''
        self.empty = True
        self.occupant = 0
        self.cost = 0

class TokenSpace(object):
    def __init__(self):
        self.name = ''
        self.color = 'none'
        self.empty = True
        self.singlton = True
        self.tokens = []

    def add_token(object, color):
        self.tokens.append(color)
        self.empty = False

    def remove_token(object, color):
        try:
            self.tokens.index(color)
        except ValueError:
            return False
        else:
            return True

def setup_tile_stack_1(stack):
    # Add blue trader cards
    for i in range(0,8):
        current_tile = {
            'category': 'trader',
            'color': 'blue',
            'hand': 'black'
            }
        stack.append(current_tile)
    # Green trader cards
    for i in range(0,8):
        current_tile = {
            'category': 'trader',
            'color': 'green',
            'hand': 'green'
            }
        stack.append(current_tile)

    # Water hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'green',
        'points': 2
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'black',
        'points': 2
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'green',
        'points': 3
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'black',
        'points': 3
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'water',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)

    # Desert hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'green',
        'points': 2
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'black',
        'points': 2
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'green',
        'points': 3
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'black',
        'points': 3
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)
    current_tile = {
        'category': 'hazard',
        'terrain': 'desert',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)

    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'green',
        'points': 2
        }
    stack.append(current_tile)
    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'black',
        'points': 2
        }
    stack.append(current_tile)
    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'green',
        'points': 3
        }
    stack.append(current_tile)
    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'black',
        'points': 3
        }
    stack.append(current_tile)
    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)
    # Rock hazards
    current_tile = {
        'category': 'hazard',
        'terrain': 'rock',
        'hand': 'green',
        'points': 4
        }
    stack.append(current_tile)

def setup_tile_stack_2(stack):
    for i in range(0,11):
        current_tile = {
            'category': 'cowboy',
            }
        stack.append(current_tile)
    for i in range(0,11):
        current_tile = {
            'category': 'builder',
            }
        stack.append(current_tile)
    for i in range(0,11):
        current_tile = {
            'category': 'engineer',
            }
        stack.append(current_tile)

def setup_tile_stack_3(stack):
    for i in range(0,7):
        current_tile = {
            'category': 'cowboy',
            }
        stack.append(current_tile)
    for i in range(0,7):
        current_tile = {
            'category': 'builder',
            }
        stack.append(current_tile)
    for i in range(0,7):
        current_tile = {
            'category': 'engineer',
            }
        stack.append(current_tile)

    # Add trader cards
    for i in range(0,3):
        current_tile = {
            'category': 'trader',
            'color': 'blue',
            'hand': 'black'
            }
        stack.append(current_tile)
    for i in range(0,3):
        current_tile = {
            'category': 'trader',
            'color': 'green',
            'hand': 'green'
            }
        stack.append(current_tile)
