import config
import setup
import action
import debug

players = 2
config.players = players

setup.setup_draw_bag()
setup.setup_players()

# Print contents of draw bag for debugging.
'''
for i in range (0, config.common_area.draw_bag.len()):
    tile = config.common_area.draw_bag.stack[i]
    print 'Tile ' + str(i) + ' ' + tile.color
'''

setup.setup_factories(config.players)

while True:
    # Loop for a round of moving tiles from pattern lines to wall.
    # First, check to see if the game is over.

    # Distribute tiles from the discard bag to the factories.
    action.deal_to_factories()
    # Loop for one round of picking up tiles.

    # Check to see if the game is over.
    if config.game_over:
        break

    i = config.starting_player
    while True:
        while i < players:
            # Check to see if the round is over.
            round_over = True
            for factory in config.common_area.factory_list:
                if not factory.empty():
                    round_over = False
                    break
            if round_over and config.common_area.center.no_colors():
                break
            else:
                round_over = False
            if round_over == True:
                break

            # Beginning of one player turn.
            action.pick_up_tiles(i)
            i += 1
        # If the round is over, move on to score the factories.
        if round_over == True:
            break
        # Begin loop over again with first player in cycle.
        i = 0

    # At the end of a round.  Move tiles to the wall.
    p = players
    action.move_to_wall(p)

    # Print player scores for debugging
    for i in range(players):
        print '  Player ' + str(i) + ' score: ' + \
            str(config.player_area_list[i].score)
        raw_input('Hit enter to continue. ')

    # Check to see if the game is over.
    if config.game_over:
        break

    # Shuffle the discard bag to prepare for next deal.
    config.common_area.discard.shuffle()

# Game over.  Display final scores.
print 'FINAL SCORES'
for i in range(players):
    print '  Player ' + str(i+1) + ': ' + \
        str(config.player_area_list[i].score)

'''
# Print factory info for debugging
factory_list = config.common_area.factory_list
for i in range(0, len(factory_list)):
    print 'FACTORY ' + str(i)
    for j in range(0, factory_list[i].len()):
        print '  ' + factory_list[i].stack[j].color
center = config.common_area.center
print 'CENTER '
for j in range(0, center.len()):
    print '  ' + center.stack[j].color
'''
