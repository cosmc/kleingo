# kleingo.py
#
# Visualizes an ASCII representation of a three-player go game on the surface
# of a Klein bottle.
#
# Usage:
# python kleingo.py <input file name>

import sys
import pygame

def main(args):
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    # Read in an ASCII description of the board to visualize.
    infile = open(args[1], "r")
    board = map(lambda x: x.replace("\n",""), infile.readlines())
    infile.close()

    # Load the appropriately sized board image.
    if len(board) == 19:
        board_img = pygame.image.load("empty_board.png").convert(32)
    elif len(board) == 13:
        board_img = pygame.image.load("empty_board13.png").convert(32)
    elif len(board) == 9:
        board_img = pygame.image.load("empty_board9.png").convert(32)

    # Determine dimensions of grid and pieces.
    board_width, board_height = board_img.get_width(), board_img.get_height()
    piece_radius = 12

    # Draw the pieces on the board.
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                continue
            elif board[i][j] == 'r':
                piece_color = (255,0,0)
            elif board[i][j] == 'g':
                piece_color = (0,255,0)
            elif board[i][j] == 'u':
                piece_color = (0,0,255)
            elif board[i][j] == 'w':
                piece_color = (255,255,255)
            elif board[i][j] == 'b':
                piece_color = (0,0,0)
            elif board[i][j] == 'c':
                piece_color = (0,255,255)
            elif board[i][j] == 'm':
                piece_color = (255,0,255)
            elif board[i][j] == 'y':
                piece_color = (255,255,0)
            pygame.draw.circle(
                board_img,
                piece_color,
                (int(round((2*j+1)*piece_radius))-j,
                    int(round((2*i+1)*piece_radius))-i),
                int(round(piece_radius))
            )

    # Tile the board across the screen.
    for y in range(0,screen.get_height()+1,board_height):

        # Flip the board at each new y value. This results in a Klein bottle
        # topology. For a toroidal board, comment out this line.
        board_img = pygame.transform.flip(board_img, True, False)

        for x in range(0,screen.get_width()+1,board_width):
            screen.blit(board_img, (x, y))

    pygame.display.flip() # Tada!

    # Main game loop.
    # Currently just enables you to quit, but we might want to use it later
    # to make the visualizer more interactive or actually playable.
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return 0
            if event.type == pygame.KEYDOWN: return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))