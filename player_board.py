import random

import tiles
import cards
import buildings

class PlayerBonusSpaces(object):
    def __init__(self, color):
        auxiliary = []
        for i in range(0,2):
            auxiliary.append([])
            current_space = tiles.TokenSpace()
            current_name = 'Auxiliary space ' + str(i+1) + ', 1'
            current_space.name = current_name
            auxiliary[i].append(current_space)
            current_space = tiles.TokenSpace()
            current_name = 'Auxiliary space ' + str(i+1) + ', 2'
            current_space.name = current_name
            current_space.color = 'white'
            current_space.empty = False
            current_space.tokens.append(color)
            auxiliary[i].append(current_space)

        for i in range(2,5):
            auxiliary.append([])
            current_space = tiles.TokenSpace()
            current_name = 'Auxiliary space ' + str(i+1) + ', 2'
            current_space.name = current_name
            current_space.color = 'white'
            current_space.empty = False
            current_space.tokens.append(color)
            auxiliary[i].append(current_space)
            current_space = tiles.TokenSpace()
            current_name = 'Auxiliary space ' + str(i+1) + ', 2'
            current_space.name = current_name
            current_space.color = 'white'
            current_space.empty = False
            current_space.tokens.append(color)
            auxiliary[i].append(current_space)

        self.auxiliary = auxiliary

        movement_bonus = []
        hand_bonus = []
        for i in range (0,2):
            current_space = tiles.TokenSpace()
            current_name = 'Movement bonus space ' + str(i+1)
            current_space.name = current_name
            current_space.color = 'black'
            current_space.empty = False
            current_space.tokens.append(color)
            movement_bonus.append(current_space)
            current_space = tiles.TokenSpace()
            current_name = 'Hand bonus space ' + str(i+1)
            current_space.name = current_name
            current_space.color = 'black'
            current_space.empty = False
            current_space.tokens.append(color)
            hand_bonus.append(current_space)
        self.movement_bonus = movement_bonus
        self.hand_bonus = hand_bonus


class PlayerCertificateSpaces(object):
    def __init__(self, color):
        self.value = 0

        current_space = tiles.TokenSpace()
        current_space.name = 'Certificate space 4'
        current_space.color = 'white'
        current_space.empty = False
        current_space.tokens.append(color)
        self.certificate_token_4 = current_space

        current_space = tiles.TokenSpace()
        current_space.name = 'Certificate space 5'
        current_space.color = 'black'
        current_space.empty = False
        current_space.tokens.append(color)
        self.certificate_token_5 = current_space

class PlayerWorkerSpace(tiles.TileSpace):
    def __init__(self):
        self.permanent = False
        self.bonus = 'none'

class PlayerCowboySpace(object):
    def __init__(self):
        self.value = 1

        cowboy_display = []
        current_space = PlayerWorkerSpace()
        current_space.permanent = True
        current_space.empty = False
        current_space.bonus = 'none'
        cowboy_display.append(current_space)
        for i in range(1,6):
            current_space = PlayerWorkerSpace()
            current_space.permanent = False
            current_space.empty = True
            if i == 3:
                current_space.bonus = 'Cowboy bonus 1'
            elif i == 5:
                current_space.bonus = 'Cowboy bonus 2'
            else:
                current_space.bonus = 'none'
            cowboy_display.append(current_space)
        self.cowboy_display = cowboy_display

class PlayerBuilderSpace(object):
    def __init__(self):
        self.value = 1

        builder_display = []
        current_space = PlayerWorkerSpace()
        current_space.permanent = True
        current_space.empty = False
        current_space.bonus = 'none'
        builder_display.append(current_space)
        for i in range(1,6):
            current_space = PlayerWorkerSpace()
            current_space.permanent = False
            current_space.empty = True
            if i == 3:
                current_space.bonus = 'Builder bonus 1'
            elif i == 5:
                current_space.bonus = 'Builder bonus 2'
            else:
                current_space.bonus = 'none'
            builder_display.append(current_space)
        self.builder_display = builder_display

class PlayerEngineerSpace(object):
    def __init__(self):
        self.value = 1

        engineer_display = []
        current_space = PlayerWorkerSpace()
        current_space.permanent = True
        current_space.empty = False
        current_space.bonus = 'none'
        engineer_display.append(current_space)
        for i in range(1,6):
            current_space = PlayerWorkerSpace()
            current_space.permanent = False
            current_space.empty = True
            current_space.bonus = 'Engineer bonus ' + str(i)
            engineer_display.append(current_space)
        self.engineer_display = engineer_display

class PlayerBoard(object):
    def __init__(self, color, player_objective_deck):
        # Location of tokens on board
        self.man = 0
        self.train = 0

        # Create the player buildings
        b = []
        buildings.setup_player_buildings(b, color)
        self.buildings = b

        # Create the player cattle card deck
        c = []
        cards.setup_player_cattle_deck(c, color)
        random.shuffle(c)

        # Create the player hand
        h = []
        cards.setup_player_hand(c, h)

        # Create an empty discard pile
        d = []

        self.cattle_deck = c
        self.hand_size = 4
        self.hand = h
        self.discard = d

        # Create the objective display and g.ive one card to each player
        obj = []
        cards.setup_player_objective_display(obj, player_objective_deck)
        self.objective_deck = obj

        # Create the auxiliary actions, movement, and hand size spaces
        bonus_spaces = PlayerBonusSpaces(color)
        self.bonus_spaces = bonus_spaces
        self.trail_moves = 3

        # Create the certificate area
        certificates = PlayerCertificateSpaces(color)
        self.certificates = certificates

        # Create the worker areas
        self.cowboy_space = PlayerCowboySpace()
        self.builder_space = PlayerBuilderSpace()
        self.engineer_space = PlayerEngineerSpace()
