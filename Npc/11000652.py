""" 11000652: Prisoner 170124 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])


