from classes.KeyBoard import KeyBoard


class Player:
    def __init__(self):
        pass

    def move_right(self):
        KeyBoard.press_right_arrow_key()

    def move_left(self):
        KeyBoard.press_left_arrow_key()

    def jump(self):
        KeyBoard.press_up_arrow_key()
