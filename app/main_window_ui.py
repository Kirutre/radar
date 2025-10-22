# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

from radar_widget import RadarWidget
from colors import radar_colors

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 600)
        MainWindow.setStyleSheet(f"""
        QLabel {{
            color: {radar_colors['LINE']};
        }}

        QPushButton {{
            background-color: transparent;

            border: 2px solid {radar_colors['LINE']};
            border-radius: 5px;

            color: {radar_colors['LINE']};
        }}

        QLineEdit {{
            background-color: transparent;

            border: 2px solid {radar_colors['LINE']};
            border-radius: 5px;

            color: {radar_colors['LINE']};
        }}

        QComboBox {{
            background-color: transparent;

            border: 2px solid {radar_colors['LINE']};
            border-radius: 5px;

            color: {radar_colors['LINE']};

            padding: 1px 18px 1px 3px;
        }}

        QComboBox::drop-down {{
            background-color: transparent;

            border: none;
        }}

        QComboBox QAbstractItemView {{
            border: 2px solid {radar_colors['LINE']};

            background-color: transparent;
            selection-background-color: {radar_colors['LINE']};

            color: {radar_colors['LINE']};
        }}""")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 3, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.change_mode_combo_box = QComboBox(self.widget_2)
        self.change_mode_combo_box.addItem("")
        self.change_mode_combo_box.addItem("")
        self.change_mode_combo_box.addItem("")
        self.change_mode_combo_box.setObjectName(u"change_mode_combo_box")

        self.gridLayout_2.addWidget(self.change_mode_combo_box, 6, 1, 1, 1)

        self.detection_distance_line_edit = QLineEdit(self.widget_2)
        self.detection_distance_line_edit.setObjectName(u"detection_distance_line_edit")

        self.gridLayout_2.addWidget(self.detection_distance_line_edit, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 5, 0, 1, 2)

        self.change_color_button = QPushButton(self.widget_2)
        self.change_color_button.setObjectName(u"change_color_button")

        self.gridLayout_2.addWidget(self.change_color_button, 4, 1, 1, 1)

        self.detection_distance_label = QLabel(self.widget_2)
        self.detection_distance_label.setObjectName(u"detection_distance_label")

        self.gridLayout_2.addWidget(self.detection_distance_label, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 2)

        self.move_widget = QWidget(self.widget_2)
        self.move_widget.setObjectName(u"move_widget")
        self.gridLayout_3 = QGridLayout(self.move_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.move_left_button = QPushButton(self.move_widget)
        self.move_left_button.setObjectName(u"move_left_button")

        self.gridLayout_3.addWidget(self.move_left_button, 1, 0, 1, 1)

        self.move_right_button = QPushButton(self.move_widget)
        self.move_right_button.setObjectName(u"move_right_button")

        self.gridLayout_3.addWidget(self.move_right_button, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.move_widget, 8, 0, 1, 2)

        self.radar_title_label = QLabel(self.widget_2)
        self.radar_title_label.setObjectName(u"radar_title_label")

        self.gridLayout_2.addWidget(self.radar_title_label, 1, 0, 1, 2)

        self.change_mode_label = QLabel(self.widget_2)
        self.change_mode_label.setObjectName(u"change_mode_label")

        self.gridLayout_2.addWidget(self.change_mode_label, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 9, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 3, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget1 = RadarWidget(self.widget)
        self.widget1.setObjectName(u"widget1")

        self.gridLayout_4.addWidget(self.widget1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 2, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 882, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Radar", None))
        self.change_mode_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Autom\u00e1tico", None))
        self.change_mode_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Manual", None))
        self.change_mode_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Seguimiento", None))

        self.change_color_button.setText(QCoreApplication.translate("MainWindow", u"Cambiar Color", None))
        self.detection_distance_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Distancia de detecci\u00f3n:</span></p></body></html>", None))
        self.move_left_button.setText(QCoreApplication.translate("MainWindow", u"Izquierda", None))
        self.move_right_button.setText(QCoreApplication.translate("MainWindow", u"Derecha", None))
        self.radar_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Controlador</span></p></body></html>", None))
        self.change_mode_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Cambiar Modo:</span></p></body></html>", None))
    # retranslateUi

