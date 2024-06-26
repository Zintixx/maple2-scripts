""" trigger/02000347_bf/guide.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[60002]):
            return 대기_02(self.ctx)


class 대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='8', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000347_BF__MAIN1__5$', duration=5000, box_ids=['0'])


initial_state = 대기
