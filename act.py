import config

def null_function():
    pass

class Action(object):
    def __init__(self):
        self.string = ''
        self.possible = null_function
        self.execute = null_function

def setup_action_dictionary(board, player_list):
    a = config.action_dictionary

    current_action = Action()
    current_action.string = 'Sell a white cow for 2 coins.'

    def f_possible():
        p = config.current_player
        # Bank must have 2 coins
        if board.bank.balance < 2:
            return False
        # Player must have a white cow.
        for space in player_list[p].hand:
            if space.occupant['color'] == 'white':
                return True
        return False
    current_action.possible = f_possible

    def f_execute():
        p = config.current_player

        # Give the player two coins
        board.bank.withdraw(2)
        player_list[p].bank += 2
        # Remove a white card from the player's hand
        for space in player_list[p].hand:
            if space.occupant['color'] == 'white':
                player_list[p].hand.remove(space)
                break
    current_action.execute = f_execute

    a['sell_white_2'] = current_action

    current_action = Action()
    current_action.string = 'Hire a worker from the labor market, regular cost.'

    def f_possible():
        p = config.current_player
        # Scan through every space in labor market array.
        # See if there is a tile that the player can afford.
        job_market = board.job_market
        player = player_list[p]

        for r in range(0, len(job_market)):
            for c in range(0, config.players):
                if not job_market[r][c].empty:
                    tile = job_market[r][c].occupant
                    if tile['category'] == 'job_market_token':
                        return False
                    else:
                        if job_market[r][c].cost <= player.bank:
                            # Player can afford tile.  See if a space is available.
                            if tile['category'] == 'cowboy':
                                if not player.cowboy_space.full():
                                    return True
                            elif tile['category'] == 'builder':
                                if not player.builder_space.full():
                                    return True
                            else:   # an engineer
                                if not player.engineer_space.full():
                                    return True
                # We have reached the end of the job market, and no tile is
                # affordable.  The job market token has been removed from the board.
                return False
    current_action.possible = f_possible

    def f_execute():
        p = config.current_player
        job_market = board.job_market
        player = player_list[p]

        # Ask player to choose tile to remove.
        [r, c] = io_choose_tile(job_market, player)

        # Skip action if player passed on choice
        if r == -1:
            return

        # Remove the tile from the job market
        tile = job_market[r][c].occupant
        job_market[r][c].occupant = 0
        job_market[r][c].empty = True

        # Deduct the cost from the player's bank
        cost = job_market[r][c].cost
        player.bank -= cost
        board.bank.deposit(cost)
    current_action.execute = f_execute

    a['buy_worker'] = current_action

    current_action = Action()
    current_action.string = 'Remove a hazard for free.'

    def f_possible():
        # See if there are any hazard tiles on the game board.
        for i in range(2,6):
            if not board.trail[i].empty:
                return True
        for i in range(12,16):
            if not board.trail[i].empty:
                return True
        for i in range(34,38):
            if not board.trail[i].empty:
                return True
        return False
    current_action.possible = f_possible

    def f_execute():
        p = config.current_player

        index = io.choose_hazard(board.trail, player_list[p])
        # Remove hazard from trail
        tile = board.trail[index].occupant
        board.trail[index].occupant = 0
        board.trail[index].empty = True
        # Add hazard to player list
        player_list[p].hazard_list.append(tile)
    current_action.execute = f_execute

    a['remove_hazard_free'] = current_action


    current_action = Action()
    current_action.string = 'Remove a trader, regular value.'

    def f_possible():
        # See if we can remove a trader at no cost
        for i in range(22,28):
            if not board.trail[i].empty:
                return True
        # See if we have enough money to buy the cheapest negative trader.
        if player.bank == 0:
            return False
        else:
            return True
    current_action.possible = f_possible

    def f_execute():
        p = config.player
        player = player_list[p]

        index = io.choose_trader(board.trail, player_list[p])
        # Remove trader from trail
        tile = board.trail[index].occupant
        board.trail[index].occupant = 0
    current_action.execute = f_execute

    a['remove_hazard_free'] = current_action


'''
def buy_worker_0(cost):
    pass

def buy_worker_min2(cost):
    pass
'''
