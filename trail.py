import random

class TrailSpace(object):
    def __init__(self, index, category, action, links):
        '''
        index:      <int> position of space on board
        category:   <str> type of space, one of 'start', 'neutral', 'player',
                    'water_hazard', 'sand_hazard','rock_hazard','trader', 'end'
        occupant:   <dict> refers to specific building, etc in the space
                    possibly use an int to refer to indices
        action_list:     <obj> list of<str> or <int> possible bonus action associated with
                    risk spaces
        links:      <list> ints containing indices for spaces that directly
                    follow this space on the trail
        '''
        self.index = index
        self.category = category
        self.action = action
        self.links = links

        self.occupant = 0
        self.empty = True
'''
    def empty(self):
        if self.occupant == 0:
            return True
        else:
            return False
'''

def find_locations(t, start, moves):
    locations = set()
    for link in t[start].links:
        # Find next space that is full or splits in two
        if t[link].index == 48:
            # in KC
            locations.add(48)
        elif t[link].empty:
            locations.update(find_locations(t, link, moves))
        else:
            locations.add(link)
            if moves > 1:
                locations.update(find_locations(t, link, moves - 1))
    return locations

def setupTrail(t):
    BONUS1 = 1
    BONUS2 = 2
    BONUS3 = 3
    BONUS4 = 4
    BONUS5 = 5
    BONUS6 = 6

    # Starting space
    current_space = TrailSpace(0, 'start', 0, [1])
    t.append(current_space)

    # Lower two segments of trail, working right-to left and bottom-to-top
    current_space = TrailSpace(1, 'neutral', 0, [2, 8])
    t.append(current_space)

    for i in range(2,6):
        current_space = TrailSpace(i, 'hazard', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(6, 'player', BONUS1, [7])
    t.append(current_space)

    current_space = TrailSpace(7, 'player', BONUS1, [11])
    t.append(current_space)

    for i in range(8,11):
        current_space = TrailSpace(i, 'player', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(11, 'neutral', 0, [12, 17])
    t.append(current_space)

    # Vertical segment of trail on bottom left, working left-to-right and
    # bottom-to-top

    for i in range(12,16):
        current_space = TrailSpace(i, 'hazard', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(16, 'player', BONUS2, [20])
    t.append(current_space)

    for i in range(17,20):
        current_space = TrailSpace(i, 'player', 0, [i+1])
        t.append(current_space)

    # Middle segment of trail

    current_space = TrailSpace(20, 'neutral', 0, [21, 31])
    t.append(current_space)

    current_space = TrailSpace(21, 'player', 0, [22, 30])
    t.append(current_space)

    for i in range(22,28):
        current_space = TrailSpace(i, 'trader', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(28, 'player', BONUS3, [29])
    t.append(current_space)

    current_space = TrailSpace(29, 'player', BONUS4, [33])
    t.append(current_space)

    current_space = TrailSpace(30, 'neutral', 0, [33])
    t.append(current_space)

    for i in range(31,33):
        current_space = TrailSpace(i, 'player', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(33, 'neutral', 0, [34, 40])
    t.append(current_space)

    # Top of trail at right

    for i in range(34,38):
        current_space = TrailSpace(i, 'hazard', 0, [i+1])
        t.append(current_space)

    current_space = TrailSpace(38, 'player', BONUS5, [39])
    t.append(current_space)

    current_space = TrailSpace(39, 'player', BONUS6, [42])
    t.append(current_space)

    for i in range(40,42):
        current_space = TrailSpace(i, 'player', 0, [i+1])
        t.append(current_space)

    # Top of trail at left

    current_space = TrailSpace(42, 'neutral', 0, [43, 44])
    t.append(current_space)

    current_space = TrailSpace(43, 'player', 0, [45])
    t.append(current_space)

    current_space = TrailSpace(44, 'player', 0, [45])
    t.append(current_space)

    current_space = TrailSpace(45, 'neutral', 0, [46, 47])
    t.append(current_space)

    current_space = TrailSpace(46, 'neutral', 0, [48])
    t.append(current_space)

    current_space = TrailSpace(47, 'player', 0, [48])
    t.append(current_space)

    # Last space on trail is Kansas City

    current_space = TrailSpace(48, 'end', 0, [0])
    t.append(current_space)

    # Extra space for negative traders, players cannot visit these

    for i in range (49,52):
        current_space = TrailSpace(i, 'trader', 0, [0])
        t.append(current_space)

# Add trader and hazard tiles to trail
def setupTrailAddTiles(ts1, trail):
    overflow = False
    for i in range(1,8):
        if overflow == True:
            ts1.append(current_tile)
            random.shuffle(ts1)
            i = i - 1
            overflow = False
        current_tile = ts1.pop()
        if current_tile['category'] == 'trader':
            # Find first non-empty trader space
            # Begin with negative spaces that lie off the trail
            if trail[51].empty == True:
                for j in range(49,52):
                    if trail[j].empty == True:
                        trail[j].occupant = current_tile
                        trail[j].empty = False
                        break
            # Otherwise insert the tile on the trader spaces on trail
            else:
                # overflow condition not possible for traders on setup
                for j in range(22,28):
                    if trail[j].empty == True:
                        trail[j].occupant = current_tile
                        trail[j].empty = False
                        break
        else:   # current tile is a hazard
            if current_tile['terrain'] == 'water':
                if trail[5].empty == False:
                    overflow = True
                    break
                else:
                    for j in range(2,6):
                        if trail[j].empty == True:
                            trail[j].occupant = current_tile
                            trail[j].empty = False
                            break
            elif current_tile['terrain'] == 'desert':
                if trail[15].empty == False:
                    overflow = True
                    break
                else:
                    for j in range(12,16):
                        if trail[j].empty == True:
                            trail[j].occupant = current_tile
                            trail[j].empty = False
                            break
            else:       # rock hazard
                if trail[37].empty == False:
                    overflow = True
                    break
                else:
                    for j in range(34,38):
                        if trail[j].empty == True:
                            trail[j].occupant = current_tile
                            trail[j].empty = False
                            break

# Add neutral buildings to trail
def setupTrailAddBuildings(n, trail):
        location_list = [1, 11, 20, 30, 33, 42, 45]
        for i in range(0,7):
            current_building = n.pop()
            current_space = location_list[i]
            trail[current_space].occupant = current_building
            trail[current_space].empty = False
