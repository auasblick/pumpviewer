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


class ColorManager:
    """
    color manager of pump viewer
    """
    def __init__(self):
        self.font: int
        self.background: int
        self.gaps: int
        self.__post_init__()

    def __post_init__(self):
        if is_dark_mode():
            self.font = 240
            self.background = 32
            self.tertiary = 0
        else:
            self.font = 0
            self.background = 240
            self.tertiary = 150
