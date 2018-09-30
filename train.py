import torch
import random

from game import Game
from agent import RLAgent
from stupid_ai import StupidAI


game = Game()
agent = RLAgent()
stupid_ai = StupidAI()

num_win = 0
num_lose = 0
num_tie = 0

random.seed(1000)


def check_board_and_may_update_state_values():
    global num_win, num_lose, num_tie
    win_or_tie = True
    if game.who_wins() == -1:  # Human win
        print('==================> You win!')
        agent.update_state_values(0)
        num_win += 1
    elif game.who_wins() == 1:  # AI win
        print('==================> You lose..')
        agent.update_state_values(1)
        num_lose += 1
    elif game.who_wins() == 2:  # Tie
        print('==================> Tie!')
        num_tie += 1
    else:
        win_or_tie = False

    if win_or_tie:
        game.clear()
        agent.clear_history()
    return win_or_tie


while True:
    print(num_win, num_lose, num_tie)
    if num_win + num_lose + num_tie == 20000:
        break

    # Stupid AI move
    x, y = stupid_ai.random_move(game.board)
    game.take_move(x, y, -1)
    print(game)

    # Check
    win_or_tie = check_board_and_may_update_state_values()
    if win_or_tie:
        continue

    # RL AI move
    x, y = agent.next_move(game.board)
    game.take_move(x, y, 1)
    agent.cache_move(game.board)
    print(game)

    # Check
    check_board_and_may_update_state_values()

torch.save(agent.state_values, 'model.pth')
