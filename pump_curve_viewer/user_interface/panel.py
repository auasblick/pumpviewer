from PySide6.QtWidgets import QWidget
from pump_curve_viewer.user_interface.color import ColorManager


class Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # obtain color palette
        __color_manager = ColorManager()
        # Apply the background and foreground colors
        self.background_color: str = f"rgb({__color_manager.background}, {__color_manager.background}, {__color_manager.background})"
        self.foreground_color: str = f"rgb({__color_manager.font}, {__color_manager.font}, {__color_manager.font})"
        self.setStyleSheet(f"background-color: {self.background_color}; color: {self.foreground_color};")


    def set_background_color(self, color: int) -> None:
        self.background_color = f"rgb({color}, {color}, {color})"
        self.setStyleSheet(f"background-color: {self.background_color}; color: {self.foreground_color};")

    def set_foreground_color(self, color: int) -> None:
        self.foreground_color = f"rgb({color}, {color}, {color})"
        self.setStyleSheet(f"background-color: {self.background_color}; color: {self.foreground_color};")
