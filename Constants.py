# used port numbers from: https://stackoverflow.com/questions/23267305/python-sockets-peer-to-peer
SERVER_PORT = 1500
CLIENT_PORT = 1501

# IP for the black computer
BLACK_IP = "172.20.10.14"

# IP for the white computer
WHITE_IP = "172.20.10.13"

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Hunt for Red October"
SCALING = 2.0

# from https://coolors.co/143b49-9e342b-e79805-e5dada-02040f
PALETTE_BLUE = "#143b49"
PALETTE_RED = "#9e342b"
PALETTE_YELLOW = "#e79805"
PALETTE_WHITE = "#e5dada"
PALETTE_BLACK = "#02040f"

REACTOR_TICK_TIME = 2
TORPEDO_TICK_TIME = REACTOR_TICK_TIME * 2
UNIT_SIZE = 10 * SCALING

SMALL_ISLAND_COUNT = 30
TALL_ISLAND_COUNT = 20
WIDE_ISLAND_COUNT = 20
LARGE_ISLAND_COUNT = 15

TAKE_REACTOR_DAMAGE = True

SHOW_RADIO = True