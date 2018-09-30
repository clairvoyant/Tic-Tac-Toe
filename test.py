import torch
import random
from game import Game
from agent import RLAgent
from stupid_ai import StupidAI

game = Game()
agent = RLAgent()
stupid_ai = StupidAI()
agent.state_values = torch.load('./model.pth')


def check_board():
    win_or_tie = True
    if game.who_wins() == -1:  # Human win
        print('==================> You win!')
        game.clear()
    elif game.who_wins() == 1:  # AI win
        print('==================> You lose..')
        game.clear()
    elif game.who_wins() == 2:  # Tie
        print('==================> Tie!')
        game.clear()
    else:
        win_or_tie = False
    return win_or_tie


while True:
    x, y = stupid_ai.human_move()
    if game.board[y, x] != 0:
        print('(%d,%d) is taken' % (x, y))
        continue

    game.take_move(x, y, -1)
    print(game)

    # Check
    win_or_tie = check_board()
    if win_or_tie:
        continue

    # RL AI move
    x, y = agent.next_move(game.board)
    game.take_move(x, y, 1)
    print(game)

    # Check
    check_board()
