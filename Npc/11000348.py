""" 11000348: Royal Guard """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180407001389$
        # - Welcome to $map:02000001$. How may I help you?
        if pick == 0:
            # $script:0831180407001390$
            # - Sell me on this $map:02000001$ business.
            return 51
        elif pick == 1:
            # $script:0831180407001391$
            # - What happened to the empress's celebration?
            return 52
        elif pick == 2:
            # $script:0831180407001392$
            # - Hey there. I'm new in town.
            # TODO: goto 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 80, 90
            return -1
        return -1

