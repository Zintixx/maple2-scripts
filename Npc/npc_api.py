import re

_state_pattern = re.compile(r"_.+__(\d+)")


class Script:
    def __init__(self, ctx):
        self.ctx = ctx
        self.states = {}

        for d in dir(self):
            result = _state_pattern.search(d)
            if result:
                id = int(result.group(1))
                self.states[id] = getattr(self, d)

    def first(self) -> int:
        """Returns the first script id for this Npc."""
        raise NotImplementedError()

    def select(self) -> int:
        """Returns the select script id for this Npc."""
        raise NotImplementedError()

    def execute(self, id: int, index: int, pick: int):
        if id in self.states:
            return self.states[id](index, pick)

        # Invalid id
        return -1

    def exit_state(self):
        """Called when the script is exited."""
        return

    def enter_state(self):
        """Called when the script is entered."""
        return

    # Script API
    def move_player(self, portal_id: int):
        self.ctx.MovePlayer(portal_id)

    def open_dialog(self, name: str, tags: str):
        self.ctx.OpenDialog(name, tags)

    def reward_item(self, rewards) -> bool:
        return self.ctx.RewardItem(rewards)

    def has_item(self, item_id: int, rarity: int = -1) -> bool:
        return self.ctx.HasItem(item_id, rarity)

    def has_mesos(self, amount: int) -> bool:
        return self.ctx.HasMesos(amount)

    def consume_meso(self, amount: int):
        return self.ctx.ConsumeMeso(amount)

    def level(self) -> int:
        return self.ctx.Level()

    def job(self) -> int:
        return self.ctx.Job()

    def job_code(self) -> int:
        return self.ctx.Job() // 10

    def current_map(self) -> int:
        return self.ctx.CurrentMap()

    def has_death_penalty(self) -> bool:
        return self.ctx.HasDeathPenalty()

    def clear_death_penalty(self):
        self.ctx.ClearDeathPenalty()
