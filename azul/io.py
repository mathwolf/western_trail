import config
import debug

def choose_tiles(p):
    # Print factory info for debugging
    factory_list = config.common_area.factory_list
    center = config.common_area.center

    # Ask the player to choose a factory.
    while True:
        print 'Player ' + str(p+1) + ', pickup tiles from one of the ' \
            + 'following locations.'
        possible_factories = []       # index of non-empty factories
        for j in range(len(factory_list)):
            output_string = ''
            if not factory_list[j].empty():
                possible_factories.append(j)
                output_string += str(len(possible_factories)) + ': FACTORY '
                for k in range(0, factory_list[j].len()):
                    output_string += factory_list[j].stack[k].color + ' '
                print output_string
        output_string = ''
        if not center.no_colors():
            possible_factories.append(-1)
            output_string += str(len(possible_factories)) + ': CENTER '
            for k in range(0, center.len()):
                output_string += center.stack[k].color + ' '
            print output_string

        selection = raw_input('Enter your choice: ')
        try:
            selection_int = int(selection)
        except ValueError:
            print 'Invalid option.  Your choice must be a number.'
            continue
        else:
            if selection_int < 1 or selection_int > len(possible_factories):
                print 'Invalid option.  Your number is out of range.'
                continue
            else:
                factory = possible_factories[selection_int - 1]
                break

    # Ask the player to choose a color of tile.
    while True:
        print 'Choose one of the available colors to pick up.'
        possible_colors = []       # index of available colors
        possible_values = []       # number of times each color occurs

        k = 0                      # count available choices
        if not factory == -1:      # choosing from a factory tile
            print 'Tiles available in factory '
            i = 0
            while i  < factory_list[factory].len():
                current_color = factory_list[factory].stack[i].color
                j = 1  # count number of tiles with current color
                while i + 1 < factory_list[factory].len() and \
                    factory_list[factory].stack[i+1].color == current_color:
                    i += 1
                    j += 1
                possible_colors.append(current_color)
                possible_values.append(j)
                k += 1
                print '  ' + str(k) + ':  ' + str(j) + ' ' + current_color
                i += 1
        else:                       # Choosing from center.
            print 'Tiles available in center'
            i = 0
            while i < center.len():
                current_color = center.stack[i].color
                if current_color == 'start':
                    i += 1
                    continue
                j = 1  # count number of tiles with current color
                while i + 1 < center.len() and \
                    center.stack[i+1].color == current_color:
                    i += 1
                    j += 1
                possible_colors.append(current_color)
                possible_values.append(j)
                k += 1
                print '  ' + str(k) + ':  ' + str(j) + ' ' + current_color
                i += 1

        selection = raw_input('Enter your choice: ')
        try:
            selection_int = int(selection)
        except ValueError:
            print 'Invalid option.  Your choice must be a number.'
            continue
        else:
            if selection_int < 1 or selection_int > len(possible_colors):
                print 'Invalid option.  Your number is out of range.'
                continue
            else:
                color = possible_colors[selection_int - 1]
                return [factory, color]


def choose_row(p, color):
    # Ask the player to choose a row.
    while True:
        possible_rows = []       # index of available rows
        j = 0                    # index for printing choices
        for i in range(5):
            current_row = config.player_area_list[p].pattern_lines[i]
            if current_row.full():
                print '  ' + str(i+1) + ": Not allowed.  Pattern line full."
                continue
            else:
                if current_row.color_allowed(color):
                    possible_rows.append(i)
                    j += 1
                    if current_row.capacity() == 1:
                        print '  ' + str(i+1) + ': Row ' + str(i+1) + ', ' \
                            + '1 space free'
                    else:
                        print '  ' + str(i+1) + ': Row ' + str(i+1) + ', ' \
                            + str(current_row.capacity()) + ' spaces free'
                else:
                    print '  ' + str(i+1) + ': Not allowed.'

        if not possible_rows:
            penalty_row = config.player_area_list[p].penalty_row
            if penalty_row.full():
                print 'No pattern lines available for this color.'
                print 'Penalty row is full.  Must discard tiles.  '
                raw_input('Hit enter to continue. ')
                return -2

            else:
                print 'No pattern lines available for this color.' \
                    '  Must place tiles in penalty row.'
                raw_input('Hit enter to continue. ')
                return -1

        print '  6: Place tiles in penalty row.'
        selection = raw_input('Select a row for your tiles: ')
        try:
            selection_int = int(selection)
        except ValueError:
            print 'Invalid option.  Your choice must be a number.'
            continue
        else:
            if selection_int < 1 or selection_int > 6:
                print 'Invalid option.  Your number is out of range.'
                continue

            # Player has chosen to put tiles in the penalty row.
            if selection_int == 6:
                return -1
            # Player has chosen a pattern line.
            try:
                possible_rows.index(selection_int - 1)
            except ValueError:
                print 'That row is not a valid choice for this color.'
                continue
            else:
                return selection_int - 1
