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
    
            # CSS
        self.setStyleSheet('''
            QPushButton {
                font-family: 'ARCADECLASSIC';
                font-size: 30px;
                background-color: white;
                color: #701A27;
                border: 2px solid #573A3D;
                border-radius: 6px;
            }
                QPushButton:hover {
                background-color: #F2D9D5;
                border: #963859; 
            }
                QPushButton:pressed {
                font-family: 'ARCADECLASSIC';
                font-size: 30px;
                background-color: #F7BAB5;
                color: #701A27;
            }
    ''')  