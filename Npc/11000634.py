""" 11000634: Prisoner 140917 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])


