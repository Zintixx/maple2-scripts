""" 11000186: Jack """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])


