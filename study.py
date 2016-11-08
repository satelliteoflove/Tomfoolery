count = 4 

def print_border():
    print('+ - - - - ' * count + ' +')

def print_filler():
    print('|         ' * count + ' |')
    print('|         ' * count + ' |')
    print('|         ' * count + ' |')
    print('|         ' * count + ' |')


def draw_grid():
    i = count
    while i > 0:
        print_border()
        print_filler()
        i -= 1

    print_border()

draw_grid()
