""" 40001060: Misplaced Book """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0901101205000090$
        # - 
        if pick == 0:
            # $script:0901101205000091$
            # - 
            # TODO: goto 201, 203
            return -1
        elif pick == 1:
            # $script:0901101205000092$
            # - 
            return 205
        return -1

    def __201(self, index: int, pick: int) -> int:
        # $script:0901101205000093$
        # - 
        if pick == 0:
            # $script:0901101205000094$
            # - 
            # TODO: goto 202
            # TODO: gotoFail 204
            return 204
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return