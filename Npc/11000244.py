""" 11000244: Mrs. Toulette """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])


