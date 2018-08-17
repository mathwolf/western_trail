import config
import player_board

def io_choose_action(action_list):
    # Return index of player choice, or -1 to skip action

    p = config.current_player
    color = player_list[p].color
    action_dict = config.action_dict

    # Ask user to pick a move
    while True:
        print 'Player ' + color + ' possible actions'
        for j in range(0, len(action_list)):
            print '  ' + str(j+1) + ': ' + action_dict[action_list[j]].string
            if not action_dict[action_list[j]].possible():
                print '  (Not possible)'
        print '  ' + str(len(action_list) + 1) + ': Skip.'
        selection = raw_input('Enter your choice: ')
        try:
            selection_int = int(selection)
        except ValueError:
            print 'Invalid option.  Your choice must be a number.'
            continue
        else:
            if selection_int < 1 or selection_int > len(action_list) + 1:
                print 'Invalid option.  Your number is out of range.'
                continue
            elif selection_int == len(action_list) + 1:
                return -1
            elif not action_dict[action_list[j]].possible():
                print 'Invalid option.  Choice is not possible at this time.'
                continue
            else:
                return selection_int - 1

def io_choose_tile(job_market, player):
    # Return list [row, column] containing location of tile to purchase.
    # Return [-1,-1] if purchase is skipped.
    p = config.current_player
    color = player_list[p].color

    # Ask user to pick a move
    while True:
        print 'Player ' + color + ' possible workers'
        i = 0   # index for number of workers available
        available_worker_location = []
        end_of_market = False

        for r in range(0, len(job_market)):
            for c in range(0, config.players):
                if not job_market[r][c].empty:
                    tile = job_market[r][c].occupant
                    if tile['category'] == 'job_market_token':
                        # end of available workers
                        end_of_market = True
                        break
                    else:
                        if job_market[r][c].cost <= player.bank:
                            # Player can afford this tile.  See if a space
                            # is available.
                            string = '  ' + str(i+1) + ': '
                            if tile['category'] == 'cowboy':
                                if not player.cowboy_space.full():
                                    string += 'cowboy, '
                                    string += ' cost '
                                    string += job_market[r][c].cost
                                    print string
                                    i += 1
                                    available_worker_location.append([r,c])
                            elif tile['category'] == 'builder':
                                if not player.builder_space.full():
                                    string += 'builder, '
                                    string += ' cost '
                                    string += job_makrket[r][c].cost
                                    print string
                                    i += 1
                                    available_worker_location.append([r,c])
                            else:   # an engineer
                                if not player.engineer_space.full():
                                    string += 'engineer, '
                                    string += ' cost '
                                    string += job_makrket[r][c].cost
                                    print string
                                    i += 1
                                    available_worker_location.append([r,c])
            if end_of_market == True:
                break
        print '  ' + str(i + 2) + ': Skip purchase.'

        selection = raw_input('Enter your choice: ')
        try:
            selection_int = int(selection)
        except ValueError:
            print 'Invalid option.  Your choice must be a number.'
            continue
        else:
            if selection_int < 1 or selection_int > i + 1:
                print 'Invalid option.  Your number is out of range.'
                continue
            elif selection_int == i + 1:
                return [-1,-1]
            else:
                return available_worker_location[selection_int - 1]


def io_choose_hazard(trail, player):
    
