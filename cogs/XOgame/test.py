import numpy as np
from cogs.XOgame.constants import *
from cogs.XOgame.utils import TicTacToe
A = np.array([[1,0,2],
              [1,2,1],
              [0,2,1]])

game = TicTacToe("inf","wof")
game.new_grid()
print(game.empty_boxes())





