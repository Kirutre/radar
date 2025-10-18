from typing import TypedDict


class QColorDict(TypedDict):
    BACKGROUND: str
    CIRCLE: str
    LINE: str
    TARGET: str
    

radar_colors: QColorDict = {
    'BACKGROUND': "#003200",
    'CIRCLE': '#00cc00',
    'LINE': '#339933',
    'TARGET': "#036903"
}
