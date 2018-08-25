import config
import debug

def setup_draw_bag():
    draw_bag = config.common_area.draw_bag
    color_list = ['red', 'yellow', 'blue', 'white', 'black']
    for i in range(0,5):
        ##################### for j in range(0,20):
        for j in range(4):
            current_tile = config.Tile()
            current_tile.color = color_list[i]
            draw_bag.add_tiles([current_tile])
    draw_bag.shuffle()
    config.common_area.draw_bag = draw_bag


def setup_players():
    p = config.players
    for i in range(p):
        current_area = config.PlayerArea()
        current_area.number = i + 1
        for j in range(5):
            current_row = config.TileRow(j + 1)
            current_area.pattern_lines.append(current_row)
        color_array = []
        color_array.append(['blue', 'yellow', 'red', 'black', 'white'])
        color_array.append(['white', 'blue', 'yellow', 'red', 'black'])
        color_array.append(['black', 'white', 'blue', 'yellow', 'red'])
        color_array.append(['red', 'black', 'white', 'blue', 'yellow'])
        color_array.append(['yellow', 'red', 'black', 'white', 'blue'])
        for j in range(5):
            current_row = config.TileRow(5)
            current_row.color_list = color_array[j]
            current_area.wall.append(current_row)
        current_area.penalty_row = config.TileRow(7)

        config.player_area_list.append(current_area)


def setup_factories(players):
    factory_list = config.common_area.factory_list
    draw_bag = config.common_area.draw_bag
    center = config.common_area.center

    ############ factory_number = 5 + 2 * (players - 1)
    factory_number = 2
    for i in range(0, factory_number):
        current_factory = config.TileStack()
        factory_list.append(current_factory)

    # Create the penalty tile and add it to the center of the board.
    start_tile = config.Tile()
    start_tile.color = 'start'
    center.add_tiles([start_tile])
    '''
    # Adapt the center so that it is considered empty if it contains only
    # the penalty tile.
    def empty_space_for_center(self, n):
        color = self.stack[n].color
        if color == 'none' or color == 'start':
            return True
        else:
            return False
    center.empty_space = empty_space_for_center
    '''



'''
    draw_bag = config.common_area.draw_bag
    for factory in factory_list:
        if draw_bag.len() >= 4:
            tile_list = draw_bag.remove_tiles(4)
            factory.add_tiles(tile_list)
        else:
            # Place remaining tiles from draw bag.
            carryover = 4 - draw_bag.len()
            tile_list = draw_bag.remove_tiles(draw_bag.len())
            factory.add_tiles(tile_list)
            if discard.empty():
                return
            discard.shuffle()
            draw_bag = discard
            discard.clear()
            if draw_bag.len() < carryover:
                factory.add_tiles(draw_bag.remove_tiles(draw_bag.len()))
                return
            else:
                factory.add_tiles(draw_bag.remove_tiles(4))
'''
