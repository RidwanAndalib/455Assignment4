from gtp_connection import GtpConnection, point_to_coord, format_point
from board_util import GoBoardUtil, PASS, where1d, BORDER, BLACK, WHITE
from board import GoBoard
import numpy as np
import argparse
import sys


class Gomoku3:
    def __init__(self, sim, sim_rule, size=7, limit=1000):
        """
        Go player that selects moves by simulation.
        """
        self.name = "Go3"
        self.version = 1.0
        self.komi = 6.5
        self.sim = sim
        self.limit = limit
        self.random_simulation = True if sim_rule == "random" else False

def run(sim, sim_rule):
    """
    Start the gtp connection and wait for commands.
    """
    board = GoBoard(7)
    con = GtpConnection(Gomoku3(sim, sim_rule), board)
    con.start_connection()


def parse_args():
    """
    Parse the arguments of the program.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--sim",
        type=int,
        default=10,
        help="number of simulations per move, so total playouts=sim*legal_moves",
    )
    parser.add_argument(
        "--simrule",
        type=str,
        default="random",
        help="type of simulation policy: random or rulebased",
    )

    args = parser.parse_args()
    sim = args.sim
    sim_rule = args.simrule

    return sim, sim_rule


if __name__ == "__main__":
    sim, sim_rule = parse_args()
    run(sim, sim_rule)
