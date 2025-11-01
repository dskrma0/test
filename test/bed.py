from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel 
from PyQt6.QtGui import QPixmap

class Bed(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.bed_image = QPixmap('bed.png')
        self.bed_image = self.bed_image.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.bed_image)
        