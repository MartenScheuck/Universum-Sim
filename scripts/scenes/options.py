from assets.variables import *
import assets.tools as tools


class Options(tools.SceneBase):
    """Options menu to change screen resolution and different stuff"""
    def __init__(self):
        tools.SceneBase.__init__(self)

    def process_input(self, events, pressed_keys):
        ...

    def update(self):
        ...

    def render(self, screen):
        screen.fill(BLACK)
        ...