import tiles

players = 3

def setupJobMarket(jm, ts2):
    jm.append([])
    for c in range(0,4):
        current_space = tiles.TileSpace()
        if c < players:
            current_tile = ts2.pop()
            current_space.occupant = current_tile
            current_space.empty = False
        jm[0].append(current_space)

    jm.append([])
    # Job market token in first space in second row
    current_space = tiles.TileSpace()
    jm_token = {'category': 'job_market_token'}
    current_space.occupant = jm_token
    current_space.empty = False
    jm[1].append(current_space)
    for c in range(1,4):
        current_space = tiles.TileSpace()
        if c < players:
            current_tile = ts2.pop()
            current_space.occupant = current_tile
            current_space.empty = False
        jm[1].append(current_space)

    for r in range(2,12):
        jm.append([])
        for c in range(0,4):
            current_space = tiles.TileSpace()
            jm[r].append(current_space)


def setupForesight(f, ts1, ts2 ,ts3):
    for r in range(0,2):
        f.append([])
        current_space = tiles.TileSpace()
        current_tile = ts1.pop()
        current_space.occupant = current_tile
        current_space.empty = False
        f[r].append(current_space)
        current_space = tiles.TileSpace()
        current_tile = ts2.pop()
        current_space.occupant = current_tile
        current_space.empty = False
        f[r].append(current_space)
        current_space = tiles.TileSpace()
        current_tile = ts3.pop()
        current_space.occupant = current_tile
        current_space.empty = False
        f[r].append(current_space)
