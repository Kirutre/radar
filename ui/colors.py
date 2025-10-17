from typing import TypedDict

from PySide6.QtGui import QColor


class QColorDict(TypedDict):
    CIRCLE: str
    LINE: str
    

radar_colors: QColorDict = {
    'CIRCLE': '#00cc00',
    'LINE': '#339933'
}