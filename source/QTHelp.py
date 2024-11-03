from PyQt6.QtWidgets import QWidget

def is_dark_mode() -> bool:
    # only applies for windows
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    return False


class Panel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # determine color based on whether dark mode is active
        if is_dark_mode():
            background_color = "rgb(32, 32, 32)"
            foreground_color = "rgb(240, 240, 240)"
        else:
            background_color = "rgb(240, 240, 240)"
            foreground_color = "rgb(0, 0, 0)"
        # Apply the background and foreground colors
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.setStyleSheet(f"background-color: {background_color}; color: {foreground_color};")


    def set_background_color(self, color):
        self.background_color = color
        self.setStyleSheet(f"background-color: {self.background_color}; color: {self.foreground_color};")

    def set_foreground_color(self, color):
        self.foreground_color = color
        self.setStyleSheet(f"background-color: {self.background_color}; color: {self.foreground_color};")
