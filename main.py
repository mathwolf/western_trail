import config
import io
import board
import player_board
import trail
import act

# Number of players
config.players = 3
players = config.players

# Setup board area and area for each player
board = board.Board()

# Display trail for debugging
print 'TRAIL'
for i in range(0,len(board.trail)):
    if board.trail[i].empty == False:
        if board.trail[i].category == 'trader':
            print str(i) + ' trader ' + board.trail[i].occupant['color']
        elif board.trail[i].category == 'hazard':
            print str(i) + ' hazard ' + board.trail[i].occupant['terrain'] \
            + ' ' + str(board.trail[i].occupant['points'])
        elif board.trail[i].category == 'neutral':
            print str(i) + ' ' + board.trail[i].occupant['name']
        else:
            print str(i) + ' something weird'
raw_input('Hit enter to continue. ')

'''
# Display job market for debugging
print 'JOB MARKET'
for r in range(0,12):
    for c in range(0,4):
        if board.job_market[r][c].empty == False:
            print str(r+1) + ',' + str(c+1) + ' ' + \
            board.job_market[r][c].occupant['category']

# Display foresight area for debugging
print 'FORESIGHT'
for r in range(0,2):
    for c in range(0,3):
            print str(r+1) + ',' + str(c+1) + ' ' + \
            board.foresight[r][c].occupant['category']

# Display cattle market for debuggging
for i in range(0,len(board.cattle_market)):
    if board.cattle_market[i].empty == False:
        print str(i) + ' ' + board.cattle_market[i].occupant['name'] + ' ' + \
        str(board.cattle_market[i].occupant['points'])
    else:
        print str(i) + ' empty'

# Show objective display for debuggging
for i in range(0,len(board.objective_display)):
    if board.objective_display[i].empty == False:
        print str(i) + ' ' + board.objective_display[i].occupant['name']
    else:
        print str(i) + ' empty'

# Display bank balance for debuggging
print 'BANK ' + str(board.bank.balance)
'''


player_list = []
color_list = ['red', 'blue', 'yellow', 'white']
for i in range(0, players):
    current_color = color_list[i]
    current_board = \
        player_board.PlayerBoard(current_color, board.player_objective_deck)
    player_list.append(current_board)

# Setup game actions
act.setup_action_dictionary(board, player_list)

# First turn allows placement in any location on trail

# Regular turn begins with player movement along trail
while True:
    for i in range(0, players):
        # Calculate legal moves along trail
        config.current_player = i

        start = player_list[i].man
        moves = player_list[i].trail_moves
        locations = list(trail.find_locations(board.trail, start, moves))
        locations.sort()
        # Ask user to pick a move
        while True:
            print 'Player ' + player_list[i].color + ' possible locations'
            for j in range(0, len(locations)):
                print '  ' + str(j+1) + ': ' \
                    + board.trail[locations[j]].category + ' ' \
                    + str(locations[j])
            selection = raw_input('Enter your choice: ')
            try:
                selection_int = int(selection)
            except ValueError:
                print 'Invalid option.  Your choice must be a number.'
                continue
            else:
                if selection_int < 1 or selection_int > len(locations):
                    print 'Invalid option.  Your number is out of range.'
                    continue
                else:
                    new_location = locations[selection_int - 1]
                    break
        # Relocate the player token
        if new_location == 48:
            print 'PLayer in KC.  Returning to start.'
            new_location = 0
        player_list[i].man = new_location
        # Follow up by taking action indicated by ending location
        current_location = board.trail[new_location].occupant
        ############
        # import pdb; pdb.set_trace()
        ############
        if current_location['category'] == 'neutral':
            current_action_list = current_location['action_list']
            while current_action_list:
                choice = io.io_choose_action(current_action_list)
                if choice == -1:
                    break
                else:
                    current_action = \
                        config.action_dict[current_action_list[choice]]
                    current_action.execute()
                    current_action_list.pop(choice)

        # Locations of players for debuggging
        for j in range(0,players):
            print 'Player ' + player_list[j].color + ' on space ' \
                + str(player_list[j].man)
        raw_input('Hit enter to continue. ')

'''
# Display player info for debugging
for i in range(0, config.players):
    print 'Player ' + str(i)
    for j in range(0, 4):
        print 'Card ' + str(j) + ' ' + player_list[i].hand[j].occupant['name']
    print 'Objectives: ' + player_list[i].objective_deck[0].occupant['name']
    # Print status of bonus token spaces
    for j in range(0,5):
        for k in range(0,2):
            if player_list[i].bonus_spaces.auxiliary[j][k].empty:
                print player_list[i].bonus_spaces.auxiliary[j][k].name \
                    + ' empty'
            else:
                print player_list[i].bonus_spaces.auxiliary[j][k].name \
                    + ' full'
    for j in range(0,2):
        if player_list[i].bonus_spaces.movement_bonus[j].empty:
            print player_list[i].bonus_spaces.movement_bonus[j].name \
                + ' empty'
        else:
            print player_list[i].bonus_spaces.movement_bonus[j].name \
                + ' full'
    for j in range(0,2):
        if player_list[i].bonus_spaces.hand_bonus[j].empty:
            print player_list[i].bonus_spaces.hand_bonus[j].name \
                + ' empty'
        else:
            print player_list[i].bonus_spaces.hand_bonus[j].name \
                + ' full'
    # Print status of certificate area
    print 'Current victory certificates: ' \
        + str(player_list[i].certificates.value)
    if player_list[i].certificates.certificate_token_4.empty:
        print player_list[i].certificates.certificate_token_4.name \
            + ' empty'
    else:
        print player_list[i].certificates.certificate_token_4.name \
            + ' full'
    if player_list[i].certificates.certificate_token_5.empty:
        print player_list[i].certificates.certificate_token_5.name \
            + ' empty'
    else:
        print player_list[i].certificates.certificate_token_5.name \
            + ' full'
    # print status of worker spaces
    for j in range(0,6):
        if not player_list[i].cowboy_space.cowboy_display[j].empty:
            print 'Cowboy space ' + str(j) + ' full'
    for j in range(0,6):
        if not player_list[i].builder_space.builder_display[j].empty:
            print 'Builder space ' + str(j) + ' full'
    for j in range(0,6):
        if not player_list[i].engineer_space.engineer_display[j].empty:
            print 'Engineer space ' + str(j) + ' full'
'''
