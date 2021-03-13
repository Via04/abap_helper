import keyboard
import pyautogui
import pyperclip

from buffer_analyzer import BufferAnalyzer


class AbapHelper:
    DEFINITION_HOTKEY = 'ctrl+alt+q'
    IMPLEMENTATION_HOTKEY = 'ctrl+alt+w'
    current_buffer = ''

    def __init__(self):
        keyboard.add_hotkey('ctrl+c', self.scan_buf())
        keyboard.add_hotkey('ctrl+alt+k', self.show_buf())
        buf_an = BufferAnalyzer(self.current_buffer)
        keyboard.add_hotkey(self.DEFINITION_HOTKEY, buf_an.create_definition())
        keyboard.add_hotkey(self.IMPLEMENTATION_HOTKEY, buf_an.create_implementation())
        keyboard.wait(']')

    def scan_buf(self):
        self.current_buffer = pyperclip.paste()
        return lambda: print(self.current_buffer)

    def show_buf(self):
        return lambda: print(self.current_buffer)


test = AbapHelper()
