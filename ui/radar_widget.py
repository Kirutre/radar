import math

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import QRectF, QSize, Qt, QTimer, QPointF, Slot

from colors import radar_colors
from serial_conection import SerialReader


class RadarWidget(QWidget):
    MAX_DISTANCE = 60
    NUM_RADIAL_LINES = 10

    def __init__(self) -> None:
        super().__init__()
        
        self.setMinimumSize(QSize(400, 250))
        
        self.serial_reader = SerialReader(port_name='COM3')
        self.serial_reader.open_port()
        
        self.targets = []
        
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_radar)
        self.animation_timer.start(50)
        
        self.serial_reader.data_received.connect(self.add_detection)

    def sizeHint(self):
        return QSize(400, 250)



    def update_radar(self) -> None:
        for target in self.targets[:]:
            target['opacity'] -= 0.05
            if target['opacity'] <= 0:
                self.targets.remove(target)
    
        self.update() 


    @Slot(int, int)
    def add_detection(self, distance: int, angle: int) -> None:
        if distance > 0 and distance <= self.MAX_DISTANCE:
            
            self.targets.append({
                'distance': distance,
                'angle': angle,
                'opacity': 1.0
            })
            
            if len(self.targets) > 50:
                self.targets.pop(0)


    def paintEvent(self, event):
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        
        center_x = self.width() / 2
        center_y = self.height()
        
        max_radius = min(center_x, center_y)
        
        self.fill_background(painter, center_x, center_y, max_radius)
        
        self.draw_circles(painter, center_x, center_y, max_radius)
        
        self.draw_diagonals(painter, center_x, center_y, max_radius)
        
        self.draw_targets(painter, center_x, center_y, max_radius)
        
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


    def fill_background(self, painter: QPainter, center_x: float, center_y: float, max_radius: float) -> None:       
        color = QColor(radar_colors['BACKGROUND'])
        color.setAlpha(50)
        
        brush_style = Qt.BrushStyle.SolidPattern
        
        brush = QBrush(color, brush_style)
        
        painter.setBrush(brush)
        
        rect_arc = QRectF(center_x - max_radius, center_y - max_radius, 2 * max_radius, 2 * max_radius)
        
        painter.drawPie(rect_arc, 0 * 16, 180 * 16)
        
    
    def draw_targets(self, painter: QPainter, center_x: float, center_y: float, max_radius: float) -> None:
        for target in self.targets:
            distance = target['distance']
            angle_deg = target['angle']
            opacity = target['opacity']
            
            distance_ratio = min(distance / self.MAX_DISTANCE, 1.0)
            target_radius = max_radius * distance_ratio
            
            
            angle_rad = math.radians(angle_deg)
            target_x = center_x + target_radius * math.cos(angle_rad)
            target_y = center_y - target_radius * math.sin(angle_rad)
            
            
            color = QColor(radar_colors['TARGET'])
            color.setAlpha(int(255 * opacity))
            
            brush = QBrush(color)
            
            painter.setBrush(brush)
            painter.setPen(Qt.PenStyle.NoPen)
            
            point_size = 6 
            painter.drawEllipse(QPointF(target_x, target_y), point_size, point_size)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
        
    window = RadarWidget()
    window.show()
    
    sys.exit(app.exec())
