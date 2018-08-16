import random

import config
import tiles
import buildings
import cards
import trail
import workers
import bank

class Board(object):
    def __init__(self):
        # Create and shuffle the tile stacks
        ts1 = []
        tiles.setup_tile_stack_1(ts1)
        random.shuffle(ts1)
        ts2 = []
        tiles.setup_tile_stack_2(ts2)
        random.shuffle(ts2)
        ts3 = []
        tiles.setup_tile_stack_3(ts3)
        random.shuffle(ts3)

        # Create and shuffle the neutral buildings
        n = []
        buildings.setup_neutral_buildings(n)
        random.shuffle(n)

        # Create the trail area of the board
        t = []
        trail.setupTrail(t)
        # Distribute the initial tiles and buildings on the trail
        trail.setupTrailAddTiles(ts1, t)
        trail.setupTrailAddBuildings(n, t)
        self.trail = t

        # Create job market area of the board
        jm = []
        workers.setupJobMarket(jm, ts2)
        self.job_market = jm

        # Create foresight area of board
        f = []
        workers.setupForesight(f, ts1, ts2, ts3)
        self.foresight = f

        # Create the shared deck of cattle cards
        cmdeck = []
        cards.setup_cattle_card_deck(cmdeck)
        random.shuffle(cmdeck)

        # Create the cattle market and deal seven cards
        cm = []
        cards.setup_cattle_market(config.players, cm, cmdeck)
        ######## add a step to sort the cattle cards for proper display
        self.cattle_market_deck = cmdeck
        self.cattle_market = cm

        # Create the shared deck of objective cards
        objdeck = []
        cards.setup_objective_deck(objdeck)
        random.shuffle(objdeck)

        # Create the deck of initial player objective cards
        player_objdeck = []
        cards.setup_player_objective_deck(player_objdeck)
        random.shuffle(player_objdeck)

        # Create the objective display area and deal four cards
        objdisp = []
        cards.setup_objective_display(objdisp, objdeck)
        self.objective_deck = objdeck
        self.objective_display = objdisp
        self.player_objective_deck = player_objdeck

        # Create the bank.  For now, we assume that all coins have size 1 unit.
        b = bank.Bank()
        self.bank = b
