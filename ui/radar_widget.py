import sys
import math

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRectF, QSize

from colors import radar_colors


class RadarWidget(QWidget):
    NUM_RADIAL_LINES = 10

    def __init__(self):
        super().__init__()
        
        self.setMinimumSize(QSize(400, 250))
        self.setStyleSheet("background-color: #1a1a1a;")

    def sizeHint(self):
        return QSize(400, 250)

    def paintEvent(self, event):
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        
        center_x = self.width() / 2
        center_y = self.height()
        
        max_radius = min(center_x, center_y)
        
        self.draw_circles(painter, center_x, center_y, max_radius)
        
        self.draw_diagonals(painter, center_x, center_y, max_radius)
        
        painter.end()


    def draw_circles(self, painter: QPainter, center_x: float, center_y: float, max_radius: float) -> None:
        for i in range(1, 11):
            radius = i * (max_radius / 10)
            
            color = QColor(radar_colors['CIRCLE'])
            
            pen = QPen(color, 2)
            
            painter.setPen(pen)
            
            rect = QRectF(center_x - radius, center_y - radius, 2 * radius, 2 * radius)
            
            painter.drawEllipse(rect)


    def draw_diagonals(self, painter: QPainter, center_x: float, center_y: float, max_radius: float) -> None:
        color = QColor(radar_colors['LINE'])
            
        pen = QPen(color, 1)
            
        painter.setPen(pen)
        
        angle_increment = 180 / (self.NUM_RADIAL_LINES + 1)
        
        for i in range(1, self.NUM_RADIAL_LINES + 1):
            angle_deg = i * angle_increment
            
            angle_rad = math.radians(angle_deg)
            
            
            end_x = center_x + max_radius * math.cos(angle_rad)
            end_y = center_y - max_radius * math.sin(angle_rad)
            
            painter.drawLine(center_x, center_y, end_x, end_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
        
    window = RadarWidget()
    window.show()
    
    sys.exit(app.exec())
