import random
import time

DEAD = 0
LIVE = 1

def dead_state(width, height):
    return [[DEAD for i in range(height)] for i in range(width)]

def random_state(width, height):
    state = dead_state(width, height)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            random_number = random.random()
            if random_number > 0.80:
                cell_state = LIVE
            else:
                cell_state = DEAD
            state[x][y] = cell_state

    return state

def state_width(state):
    return len(state)

def state_height(state):
    return len(state[0])

def next_cell_value(cell_coords, state):
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    for x1 in range((x-1), (x+1)+1):
        if x1 < 0 or x1 >= width: 
            continue

        for y1 in range((y-1), (y+1)+1):
            if y1 < 0 or y1 >= height: 
                continue
            if x1 == x and y1 == y: 
                continue

            if state[x1][y1] == LIVE:
                n_live_neighbors += 1

    if state[x][y] == LIVE:
        if n_live_neighbors <= 1:
            return DEAD
        elif n_live_neighbors <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if n_live_neighbors == 3:
            return LIVE
        else:
            return DEAD

def next_board_state(init_state):
    width = state_width(init_state)
    height = state_height(init_state)
    next_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), init_state)

    return next_state

def render(state):
    display_as = {
        DEAD: ' ',
        LIVE: u"\u2588"
    }
    lines = []
    for y in range(0, state_height(state)):
        line = ''
        for x in range(0, state_width(state)):
            line += display_as[state[x][y]]
        lines.append(line)
    print("\n".join(lines))


def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

if __name__ == "__main__":
    init_state = random_state(100, 100)
    run_forever(init_state)