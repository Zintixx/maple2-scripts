""" 11000041: Rekk """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        x = self.job()//10
        if self.level() >= 10 and x == 1:
            return 1
        if x == 10:
            return 30
        if x == 20:
            return 20
        return x + 10

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000063$
            # - Argh, this place is so boring, it's driving me crazy! If it weren't for the War Chief's order, I would be cracking skulls on Vayar Mountain and having a blast! Hey, you look pretty tough. How are you in a fight?
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000064$
            # - With a greatsword in our hands, we're fearless in battle. We can be overzealous sometimes, but that's inevitable when you've got our passion for fighting. So, how'd you like to swear fealty to the War Chief and walk the path of the Berserker?
            return -1
        return -1
