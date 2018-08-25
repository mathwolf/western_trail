import config
import io
import debug
from operator import attrgetter

def deal_to_factories():
    factory_list = config.common_area.factory_list
    draw_bag = config.common_area.draw_bag
    discard = config.common_area.discard

    # Check to see if we have a game over condition.
    if draw_bag.len() == 0 and discard.len() == 0:
        config.game_over = True
        return

    for i in range(len(factory_list)):
        if draw_bag.len() >= 4:
            tile_list = draw_bag.remove_tiles(4)
            tile_list = sorted(tile_list, key=attrgetter('color'), \
                reverse = True)
            factory_list[i].add_tiles(tile_list)
        else:
            tile_list = draw_bag.remove_tiles(draw_bag.len())
            remainder = 4 - len(tile_list)
            # Shuffle the discard bag and add it to the draw bag.
            if discard.len() == 0:
                # Return to play with incomplete factories.
                tile_list = sorted(tile_list, key=attrgetter('color'), \
                    reverse = True)
                factory_list[i].add_tiles(tile_list)
                break
            discard_tiles = discard.remove_tiles(discard.len())
            draw_bag.add_tiles(discard_tiles)
            draw_bag.shuffle()
            if draw_bag.len() >= remainder:
                tile_list.extend(draw_bag.remove_tiles(remainder))
            else:
                tile_list.extend(draw_bag.remove_tiles(draw_bag.len()))
            tile_list = sorted(tile_list, key=attrgetter('color'), \
                reverse = True)
            factory_list[i].add_tiles(tile_list)

def add_to_penalty(p, color, n):
    # Add n tiles of the given color to the penalty row.  Return the
    # number of tiles remaining after the penalty row is full.
    capacity = config.player_area_list[p].penalty_row.capacity()
    remainder = 0

    if n > capacity:
        remainder = n - capacity
        n = capacity

    for i in range(n):
        config.player_area_list[p].penalty_row.add_tile(color)

    if remainder > 0:
        for i in range(remainder):
            config.common_area.discard.add_tiles([color])


def add_to_row(p, r, color, n):
    # Add n tiles of the given color to row r.  Return the
    # number of tiles remaining after the penalty row is full.
    capacity = config.player_area_list[p].pattern_lines[r].capacity()
    remainder = 0

    if n > capacity:
        remainder = n - capacity
        n = capacity

    for i in range(n):
        config.player_area_list[p].pattern_lines[r].add_tile(color)

    if remainder > 0:
        add_to_penalty(p, color, remainder)


def pick_up_tiles(p):
    factory_list = config.common_area.factory_list
    center = config.common_area.center
    discard = config.common_area.discard

    # Get factory, color for player pick up
    [factory_index, color] = io.choose_tiles(p)

    # Remove the tiles from the given factory.
    if not factory_index == -1:
        factory = factory_list[factory_index]
        n = factory.remove_tile_color(color)
        # All remaining tiles go to the center.
        remaining_tiles = factory.remove_tiles(factory.len())
        center.add_tiles(remaining_tiles)
        center.stack = sorted(center.stack, key=attrgetter('color'))

    else:
        # If the center contains the starting tile, move it to the player's
        # penalty row.
        for i in range(center.len()):
            if center.stack[i].color == 'start':
                center.stack.pop(i)
                add_to_penalty(p, 'start', 1)
                break
        n = center.remove_tile_color(color)

    # Add the tiles to the player row
    r = io.choose_row(p, color)
    if r >= 0:
        add_to_row(p, r, color, n)
    elif r == -1:
        add_to_penalty(p, color, n)
    else:
        for i in range(n):
            discard.add_tiles([color])

def score_wall(p, i, j):
    wall = config.player_area_list[p].wall

    col_score = 1
    # upward
    k = i - 1
    while k >= 0 and not wall[k].empty_space(j):
        col_score += 1
        k -= 1
    # downward
    k = i + 1
    while k < 5 and not wall[k].empty_space(j):
        col_score += 1
        k += 1

    # leftward
    row_score = 1
    k = j - 1
    while k >= 0 and not wall[i].empty_space(k):
        row_score += 1
        k -= 1
    k = j + 1
    while k < 5 and not wall[i].empty_space(k):
        row_score += 1
        k += 1
    # Check for game ending condition.
    if row_score == 5:
        config.game_over = True

    if col_score == 1:
        return row_score
    elif row_score == 1:
        return col_score
    else:
        return row_score + col_score

def move_to_wall(players):
    # Move the first tile in each full row to its corresponding space on the
    # wall.  The remaining tiles go in the discard bag.
    for p in range(players):
        score = 0
        for i in range(5):
            current_row = config.player_area_list[p].pattern_lines[i]
            current_wall_row = config.player_area_list[p].wall[i]
            if current_row.full():
                current_color = current_row.stack[0].color
                # Add to forbidden colors for this row.
                current_row.forbidden_colors.append(current_color)
                current_row.remove_tile(0)
                j = 0
                while not current_wall_row.color_list[j] == current_color:
                    j += 1
                current_wall_row.add_tile(current_color, j)
                score += score_wall(p, i, j)
                if not i == 0:
                    # Clear out remaining tiles in row.
                    for k in range(1,current_row.len()):
                        current_color = current_row.stack[k].color
                        current_row.remove_tile(k)
                        current_tile = config.Tile()
                        current_tile.color = current_color
                        config.common_area.discard.add_tiles([current_tile])

        # Score penalty row
        penalty_row = config.player_area_list[p].penalty_row
        penalty_list = [1, 1, 2, 2, 2, 3, 3]
        for i in range(7):
            if penalty_row.empty_space(i):
                break
            score -= penalty_list[i]
            current_color = penalty_row.stack[i].color
            if  current_color == 'start':
                start_tile = config.Tile()
                start_tile.color = 'start'
                config.common_area.center.add_tiles([start_tile])
                config.starting_player = p
            else:
                current_tile = config.Tile()
                current_tile.color = current_color
                config.common_area.discard.add_tiles([current_tile])
            penalty_row.remove_tile(i)

        config.player_area_list[p].score += score
        if config.player_area_list[p].score < 0:
            config.player_area_list[p].score = 0


def calculate_bonus():
    players = config.players

    for p in range(players):
        pattern_lines = config.player_area_list[p].pattern_lines
        wall = config.player_area_list[p].wall
        score = config.player_area_list[p].score

        # Check each row to see if it is full.
        for i in range(5):
            row_bonus = True
            # Check each space in row i to see if it is empty
            for j in range(5):
                if wall[i].empty_space(j):
                    row_bonus = False
                    break
            if row_bonus == True:
                score += 2

        # Check each col to see if it is full.
        for j in range(5):
            col_bonus = True
            # Check each space in row i to see if it is empty
            for i in range(5):
                if wall[i].empty_space(j):
                    col_bonus = False
                    break
            if col_bonus == True:
                score += 7

        # Check to see if player earned a bouns for 5 tiles with the same
        # color.
        color_list = ['red', 'blue', 'black',  'white', 'yellow']
        for j in range(5):
            color_bonus = True
            # Check each row to see if it contains color j in the list.
            for i in range(5):
                try:
                    pattern_lines[i].forbidden_colors.index(color_list[j])
                except ValueError:
                    color_bonus = False
                    break
            if color_bonus == True:
                score += 10

        config.player_area_list[p].score = score
