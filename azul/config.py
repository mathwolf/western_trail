import random
import debug

players = 0
starting_player = 0
game_over = False

# Classes for tile, tile_list, tile_stack, tile_row
class Tile(object):
    def __init__(self):
        self.color = 'none'


class TileRow(object):
    def __init__(self, n):
        self.length = n
        self.stack = []
        for i in range(0,n):
            self.stack.append(Tile())
        self.color_list = []
        self.forbidden_colors = []

    def len(self):
        return len(self.stack)

    def empty_space(self, n):
        # Determine if space n is empty.
        if self.stack[n].color == 'none':
            return True
        else:
            return False

    def empty(self):
        for i in range(0, self.len()):
            if not self.empty_space(i):
                return False
        return True

    def full(self):
        for i in range(0, self.len()):
            if self.empty_space(i):
                return False
        return True

    def capacity(self):
        c = 0
        for i in range(0, self.len()):
            if self.empty_space(i):
                c += 1
        return c


    def add_tile(self, color, n = -1):
        # Insert tile in space n of list.  Assumes we have already checked
        # that the space is empty.
        # n = 0 means to put the tile in the first empty space
        if not n == -1:
            self.stack[n].color = color
        else:
            for i in range(self.len()):
                if self.empty_space(i):
                    self.stack[i].color = color
                    break

    def remove_tile(self, n):
        # Remove the tile in space n and return its color.  Assues we have
        # already checked that the space is empty.
        color = self.stack[n].color
        self.stack[n].color = 'none'
        return color

    def color_allowed(self, color):
        for c in self.forbidden_colors:
            if color == c:
                return False
        if self.empty():
            return True
        else:
            for i in range(self.len()):
                if self.stack[i].color == color:
                    return True
        return False


class TileStack(object):
    def __init__(self):
        self.stack = []

    def len(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return False
        else:
            return True

    def no_colors(self):
        if self.empty():
            return True
        if self.len() == 1 and self.stack[0].color == 'start':
            return True

    def add_tiles(self, tile_list):
        while tile_list:
            current_tile = tile_list.pop()
            self.stack.append(current_tile)

    def remove_tiles(self, n):
        # Return a list containing the next n items in the stack.
        # If there are less than n items, return all available items.
        tile_list = []
        while self.stack:
            current_tile = self.stack.pop()
            tile_list.append(current_tile)
            if len(tile_list) == n:
                return tile_list
        return tile_list


    def contains_tiles(self, color):
        # Return number of tiles in stack with given color
        n = 0
        for t in self.stack:
            if t.color == color:
                n += 1
        return n

    def remove_tile_color(self, color):
        # Assumes we have already checked that this is a legal move.
        n = 0
        i = 0

        i = 0
        while not self.stack[i].color == color:
            i += 1
        while i < self.len() and self.stack[i].color == color:
            self.stack.pop(i)
            n += 1
        return n

    def shuffle(self):
        random.shuffle(self.stack)

'''    def sort(self):
        # Sort tiles by color.
        color_list = []
        for i in range(self.len()):
            color_list.append(self.stack[i].color)
        color_list.sort()
        for i in range(self.len()):
            self.stack[i].color = color_list[i]
'''

# Access to draw and discard bags, common area, and list of player boards.

class CommonArea(object):
    def __init__(self):
        self.draw_bag = TileStack()
        self.discard = TileStack()

        self.factory_list = []
        self.center = TileStack()

common_area = CommonArea()

class PlayerArea(object):
    def __init__(self):
        self.number = 0
        self.score = 0

        self.pattern_lines = []
        self.wall = []

        self.penalty_row = 0

player_area_list = []
