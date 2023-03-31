from typing import NamedTuple
import win32api
import dataclasses
import win32con
import enum

KEY_PRESS = 0
KEY_RELEASE = win32con.KEYEVENTF_KEYUP


class KeyboardKeyMapping(enum.IntEnum):
    VK_LEFT: int = 0x25
    VK_UP: int = 0x26
    VK_RIGHT: int = 0x27
    VK_DOWN: int = 0x28


class KeyEventParams(NamedTuple):
    virtual_key_code: int
    hardware_scan_for_key: int
    flags: int
    extra_into: int


@dataclasses.dataclass
class KeyStroke:
    LEFT_PRESS = KeyEventParams(
        virtual_key_code=KeyboardKeyMapping.VK_LEFT,
        hardware_scan_for_key=0,
        flags=KEY_PRESS,
        extra_into=0,
    )
    LEFT_RELEASE = KeyEventParams(KeyboardKeyMapping.VK_LEFT, 0, KEY_RELEASE, 0)
    RIGHT_PRESS = KeyEventParams(KeyboardKeyMapping.VK_RIGHT, 0, KEY_PRESS, 0)
    RIGHT_RELEASE = KeyEventParams(KeyboardKeyMapping.VK_RIGHT, 0, KEY_RELEASE, 0)
    UP_PRESS = KeyEventParams(KeyboardKeyMapping.VK_UP, 0, KEY_PRESS, 0)
    UP_RELEASE = KeyEventParams(KeyboardKeyMapping.VK_UP, 0, KEY_RELEASE, 0)
    DOWN_PRESS = KeyEventParams(KeyboardKeyMapping.VK_DOWN, 0, KEY_PRESS, 0)
    DOWN_RELEASE = KeyEventParams(KeyboardKeyMapping.VK_DOWN, 0, KEY_RELEASE, 0)


class KeyBoard:
    @staticmethod
    def press_right_arrow_key():
        win32api.keybd_event(*KeyStroke.RIGHT_PRESS)
        win32api.keybd_event(*KeyStroke.LEFT_RELEASE)

    @staticmethod
    def press_left_arrow_key():
        win32api.keybd_event(*KeyStroke.LEFT_PRESS)
        win32api.keybd_event(*KeyStroke.RIGHT_RELEASE)

    @staticmethod
    def press_up_arrow_key():
        win32api.keybd_event(*KeyStroke.UP_PRESS)
