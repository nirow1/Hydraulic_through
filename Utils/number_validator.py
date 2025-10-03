import re

from PySide6.QtGui import QValidator


class NumberValidator(QValidator):
    def __init__(self, max_val = 1000000):
        super().__init__()
        self.max = max_val


    def validate(self, input_str, pos):
        input_str = input_str

        if input_str == "":
            return QValidator.State.Acceptable

        if input_str == "-":
            return QValidator.State.Acceptable

        try:
            val = int(input_str)
            if val <= self.max:
                return QValidator.State.Acceptable
            else:
                return QValidator.State.Invalid
        except ValueError:
            return QValidator.State.Invalid

class FloatValidator(QValidator):
    def __init__(self,min=-1000000, max=1000000, parent=None):
        super().__init__(parent)
        self.min = min
        self.max = max

    def validate(self, input_str, pos):
        input_str = input_str

        if input_str == "":
            return QValidator.State.Acceptable

        if input_str == "-":
            return QValidator.State.Acceptable

        try:
            val = float(input_str)
            if self.min <= val <= self.max:
                return QValidator.State.Acceptable
            else:
                return QValidator.State.Invalid
        except ValueError:
            return QValidator.State.Invalid