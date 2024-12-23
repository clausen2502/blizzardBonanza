import pygame
import random
from blizzard_bonanza import UI
class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.balance = 1000
        self.bet = 10
        self.ui = UI()
        self.symbols = None  # Stores the result of the spin
        self.last_payout = 0  # Stores the last payout

    def spin(self):
        pass

    def run(self):
        """Main game loop."""
