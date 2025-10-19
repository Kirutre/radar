from typing import TypedDict


class QColorDict(TypedDict):
    BACKGROUND: str
    CIRCLE: str
    LINE: str
    TARGET: str
    

radar_colors: QColorDict = {
    'BACKGROUND': "#003200",
    'CIRCLE': '#00CC00',
    'LINE': '#339933',
    'TARGET': "#04FF04",
    'SWEEP': "#19A119"
}
