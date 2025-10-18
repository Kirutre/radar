from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QObject, Signal, QIODevice


class SerialReader(QObject):
    data_received = Signal(int, int)
    
    def __init__(self, port_name: str, baud_rate: int = 9600) -> None:
        super().__init__()
        
        self.serial_port = QSerialPort()
        self.serial_port.setPortName(port_name)
        self.serial_port.setBaudRate(baud_rate)
        
        self.serial_port.readyRead.connect(self.handle_serial_data)
    
    
    def open_port(self) -> None:
        if self.serial_port.isOpen():
            print("INFO: El puerto ya está abierto.")
            
            return True
        
        # Solo lectura
        if self.serial_port.open(QIODevice.ReadOnly):
            print(f"INFO: Conectado a {self.serial_port.portName()} exitosamente.")
            
            self.serial_port.clear()
            
            return True
        
        else:
            print(f"ERROR: No se pudo abrir el puerto: {self.serial_port.errorString()}")
            
            return False


    def close_port(self) -> None:
        if self.serial_port.isOpen():
            self.serial_port.close()
            
            print("INFO: Puerto serial cerrado.")


    def handle_serial_data(self) -> None:
        while self.serial_port.canReadLine():
            try:
                data_line = self.serial_port.readLine()
                
                data_str = str(data_line, 'utf-8').strip()
                
                data_list = data_str.split(',')

                distance = int(data_list[0])
                angle = int(data_list[1])
                
                self.data_received.emit(distance, angle)
                
            except Exception as e:
                print(f"ERROR al procesar datos seriales: {e}")

     
if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    import sys

    PORT_NAME = 'COM3' 

    if PORT_NAME:
        print(f"Intentando usar el puerto: {PORT_NAME}")
        app = QApplication(sys.argv)
        
        reader = SerialReader(port_name=PORT_NAME)
        
        if reader.open_port():
            sys.exit(app.exec())
            
        else:
            print("Fallo al abrir el puerto. Terminando aplicación.")
            
    else:
        print("ERROR: No se encontraron puertos seriales disponibles.")
    