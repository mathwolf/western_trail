import config
import board
import player_board

# Number of players
config.players = 3
players = config.players

# Setup board area and area for each player
board = board.Board()
player_list = []
for i in range(0, players):
    current_board = \
        player_board.PlayerBoard('green', board.player_objective_deck)
    player_list.append(current_board)

# First turn allows placement in any location on trail

# Regular turn begins with player movement along trail
for i in range(0, players):
    # Calculate legal moves along trail

    # Ask user to pick a move

    # Follow up by taking action indicated by ending location

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
