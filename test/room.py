from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import Qt
from teto import Teto
from bed import Bed

# ----- класс комнаты ----- #
class Room(QWidget):
    def __init__(self):
        super().__init__()
        
        self.bed = Bed(self)
        self.bed.move(30, 200)
        
        self.teto = Teto(self)
        self.teto.move(200, 260)
        
        
        self.button_back = QPushButton('Back to menu', self)
        self.button_back.move(10, 10)
        self.button_back.setFixedSize(210, 30)

        self.setObjectName('room_widget')
        self.setStyleSheet('''
            #room_widget {
            background-image: url("room_background.png");
            background-repeat: no-repeat;
            background-position: center;
            }
        ''')