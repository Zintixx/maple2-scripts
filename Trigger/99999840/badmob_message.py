""" trigger/99999840/badmob_message.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=911) == 1:
            return 쫄몹1(self.ctx)
        if self.dungeon_variable(var_id=912) == 1:
            return 쫄몹2(self.ctx)
        if self.dungeon_variable(var_id=913) == 1:
            return 쫄몹3(self.ctx)


class 쫄몹1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='방해쫄몹1이 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 쫄몹2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='방해쫄몹2가 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 쫄몹3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='방해쫄몹3이 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
