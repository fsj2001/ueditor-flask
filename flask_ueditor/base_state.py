"""
Create by yy on 2019-07-24
"""
from .app_info import AppInfo
from .state import State


class BaseState(State):
    def __init__(self, state, info_code):
        super().__init__()
        self.state = state
        self._info = AppInfo.get_state_info(info_code)

    def __del__(self):
        pass

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def __dict__(self):
        return {
            "state": self.state,
            "info": self.info
        }
