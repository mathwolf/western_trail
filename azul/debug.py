import config

def show_player(p):
    player = config.player_area_list[p]

    print 'SCORE: ' + str(player.score)
    print 'PATTERN LINES'
    for i in range(5):
        string = ''
        for j in range(i+1):
            string += player.pattern_lines[i].stack[j].color + ' '
        print '  Line ' + str(i) + ': ' + string
    string = ''
    for i in range(7):
        string += player.penalty_row.stack[i].color + ' '
    print '  Penalty : ' + string

    print 'WALL'
    for i in range(5):
        string = ''
        for j in range(5):
            string += player.wall[i].stack[j].color + ' '
        print '  Line ' + str(i) + ': ' + string

def show_common():
    f_list = config.common_area.factory_list
    center = config.common_area.center

    print 'FACTORIES'
    for i in range(len(f_list)):
        string = ''
        for j in range(f_list[i].len()):
            current_color = f_list[i].stack[j].color
            string += current_color + ' '
        print 'Factory ' + str(i) + ': ' + string
    string = ''
    for i in range(center.len()):
        current_color = center.stack[i].color + ' '
        string += current_color
    print 'Center: ' + string

def show_bags():
    draw = config.common_area.draw_bag
    discard = config.common_area.discard

    print 'DRAW'
    string = ''
    for i in range(draw.len()):
        string += draw.stack[i].color + ' '
    print string
    print 'DISCARD'
    string = ''
    for i in range(discard.len()):
        string += discard.stack[i].color + ' '
    print string
