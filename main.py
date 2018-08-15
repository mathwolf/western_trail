import board

# Number of players
players = 3

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
