from PySide6.QtWidgets import QMainWindow, QMessageBox

from main_window_ui import Ui_MainWindow

from modes import Modes


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.move_widget.setVisible(False)
        
        self.detection_distance_line_edit.setText(str(self.widget1.max_distance))

        self.set_auto_repeat_buttons()

        self.set_listeners()


    def set_auto_repeat_buttons(self) -> None:
        self.move_left_button.setAutoRepeat(True)
        self.move_left_button.setAutoRepeatInterval(50)

        self.move_right_button.setAutoRepeat(True)
        self.move_right_button.setAutoRepeatInterval(50)


    def set_listeners(self) -> None:
        self.change_detection_distance_button.clicked.connect(self.change_detection_distance)
        
        self.change_color_combo_box.currentIndexChanged.connect(self.change_color)

        self.move_left_button.pressed.connect(
            lambda: (self.move_radar('2'), self.move_right_button.setEnabled(True))
        )
        self.move_right_button.pressed.connect(
            lambda: (self.move_radar('1'), self.move_left_button.setEnabled(True))
        )

        self.move_left_button.released.connect(self.stop_radar)
        self.move_right_button.released.connect(self.stop_radar)

        self.change_mode_combo_box.currentIndexChanged.connect(self.set_mode)


    def change_color (self, index: int) -> None:
        if index == 0:           
            self.widget1.radar_colors = {
                'BACKGROUND': "#003200",
                'CIRCLE': '#00CC00',
                'LINE': '#339933',
                'TARGET': "#04FF04",
                'SWEEP': "#19A119"
            }
        elif index == 1:            
            self.widget1.radar_colors = {
                'BACKGROUND': "#590D22",
                'CIRCLE': '#800F2F',
                'LINE': '#A4133C',
                'TARGET': "#C9184A",
                'SWEEP': "#FF4D6D"
            }
        elif index == 2:
            self.widget1.radar_colors = {
                'BACKGROUND': "#132E32",
                'CIRCLE': '#53A2BE',
                'LINE': '#53A2BE',
                'TARGET': "#1D84B5",
                'SWEEP': "#176087"
            }
            
        self.setStyleSheet(f"""
        QLabel {{
            color: {self.widget1.radar_colors['LINE']};
        }}

        QPushButton {{
            background-color: transparent;

            border: 2px solid {self.widget1.radar_colors['LINE']};
            border-radius: 5px;

            color: {self.widget1.radar_colors['LINE']};
        }}

        QLineEdit {{
            background-color: transparent;

            border: 2px solid {self.widget1.radar_colors['LINE']};
            border-radius: 5px;

            color: {self.widget1.radar_colors['LINE']};
        }}

        QComboBox {{
            background-color: transparent;

            border: 2px solid {self.widget1.radar_colors['LINE']};
            border-radius: 5px;

            color: {self.widget1.radar_colors['LINE']};

            padding: 1px 18px 1px 3px;
        }}

        QComboBox::drop-down {{
            background-color: transparent;

            border: none;
        }}

        QComboBox QAbstractItemView {{
            border: 2px solid {self.widget1.radar_colors['LINE']};

            background-color: transparent;
            selection-background-color: {self.widget1.radar_colors['LINE']};

            color: {self.widget1.radar_colors['LINE']};
        }}""")


    def change_detection_distance (self) -> None:
        detection_distance = int(self.detection_distance_line_edit.text())

        if not detection_distance:
            QMessageBox.critical(self, 'Distancia incorrecta', 'No se ingreso ninguna distancia')

            return

        if detection_distance < 1:
            QMessageBox.critical(self, 'Distancia incorrecta', 'La distancia debe ser mayor a 0 cm')

            return

        if detection_distance > 200:
            QMessageBox.critical(self, 'Distancia incorrecta', 'La distancia debe ser menor a 200 cm')

            return

        self.widget1.max_distance = detection_distance


    def move_radar(self, direction: str) -> None:        
        if direction == '2' and self.widget1.sweep_angle <= 1:
            print('El movimiento supera los limites del servomotor')

            self.move_left_button.setEnabled(False)

            return

        if direction == '1' and self.widget1.sweep_angle >= 179:
            print('El movimiento supera los limites del servomotor')

            self.move_right_button.setEnabled(False)

            return

        self.widget1.serial_reader.send_data(direction)


    def stop_radar(self) -> None:
        self.widget1.serial_reader.send_data('0')


    def set_mode(self, index: int) -> None:
        if index == 0:
            self.widget1.serial_reader.send_data(Modes.AUTOMATIC)

            self.move_widget.setVisible(False)
        elif index == 1:
            self.widget1.serial_reader.send_data(Modes.MANUAL)

            self.move_widget.setVisible(True)
        elif index == 2:
            self.widget1.serial_reader.send_data(Modes.FOLLOW)
            
            self.move_widget.setVisible(False)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())