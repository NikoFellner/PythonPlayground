from tkinter import Tk

from src.services.user_interface import UserInterface


class UserInterfaceService:
    def __init__(self):
        self._width = 640
        self._height = 480
        self.running_ui = Tk()
        self._ui = UserInterface()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def start(self):
        self._base_screen()
        self._ui.setup_screen(self.running_ui)
        self.running_ui.mainloop()

    def _base_screen(self) -> None:
        self.running_ui.geometry(f"{self._width}x{self._height}")
        self.running_ui.title("DuelBase")


if __name__ == "__main__":
    ui = UserInterfaceService()
    ui.start()
