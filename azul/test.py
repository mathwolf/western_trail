import config
import action
import debug
import setup

# Test calculation of bonus points
config.players = 1
p = 0

setup.setup_players()

pattern_lines = config.player_area_list[p].pattern_lines
wall = config.player_area_list[p].wall

# Set up test tiles
'''
test_stack = []
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow', 'red', 'black', 'white'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow', 'red', 'white', 'black'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['black', 'yellow', 'red'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow', 'black', 'white'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['black', 'yellow', 'white'])
test_stack.append(current_row)
'''

test_stack = []
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow', 'black'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow', 'red', 'white', 'black'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue', 'yellow'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue'])
test_stack.append(current_row)
current_row = config.TileStack()
current_row.add_tiles(['blue', 'white'])
test_stack.append(current_row)

# Set effect of wall tiles on forbidden tile list
for i in range(5):
    for j in range(test_stack[i].len()):
        pattern_lines[i].forbidden_colors.append(test_stack[i].stack[j])

# Move test tiles to the wall.
for i in range(5):
    while not test_stack[i].empty():
        current_tile = test_stack[i].remove_tiles(1)
        current_color = current_tile[0]
        for j in range(5):
            if wall[i].color_list[j] == current_color:
                wall[i].add_tile(current_color, j)
                break
# Score the wall and show the result
action.calculate_bonus()
print 'BONUS SCORES'
for i in range(config.players):
    print '  Player ' + str(i+1) + ': ' + \
        str(config.player_area_list[i].score)
