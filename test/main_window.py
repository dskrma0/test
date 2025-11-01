import warnings
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFontDatabase
from room import Room

# чтобы иконка отображалась в панели задач
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

warnings.filterwarnings("ignore", category=DeprecationWarning)


# класс меню
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
        
        # шрифты для CSS
        font_files = [
            'ARCADECLASSIC.ttf',
            'Game Paused DEMO.ttf'
        ]
        
        self.loaded_families = []
        for font_file in font_files:
            font_id = QFontDatabase.addApplicationFont(font_file)
            if font_id >= 0:
                families = QFontDatabase.applicationFontFamilies(font_id)
                if families:
                    self.loaded_families.append(families[0]) 
    
    
    def initializeUI(self):
        self.setFixedSize(QSize(500, 400))
        self.setWindowTitle('Teto something something')
        self.setWindowIcon(QIcon('icon.png'))
        self.setUpMainWindow()
        self.show()
    
    
    def setUpMainWindow(self):
        
        # центральный виджет
        self.central_menu = QWidget()
        self.setCentralWidget(self.central_menu)
        self.central_menu.setContentsMargins(20, 20, 20, 20)
        
        
        # название 
        header = QLabel('Random\ntest', self)
        header.setAlignment(Qt.AlignmentFlag.AlignTop)
        header.setFixedHeight(50)
        header.setMinimumHeight(80)
        
        
        # кнопки меню
        self.start_button = QPushButton('Start')
        self.settings_button = QPushButton('Settings')
        self.exit_button = QPushButton('Exit')
        for button in (self.start_button, self.settings_button, self.exit_button):
            button.setFixedHeight(50)
            button.setFixedWidth(170)
            
        
        # картинка в меню
        pixmap = QPixmap('teto_menu.png')
        self.image = QLabel(self)
        self.image.setPixmap(pixmap)
        self.image.setFixedSize(250, 250)
        
        
        # сигналы для кнопок меню
        self.start_button.clicked.connect(self.click_start)
        self.settings_button.clicked.connect(self.click_settings)
        self.exit_button.clicked.connect(self.click_exit)
        
        
        # кастомный курсор
        pixmap = QPixmap('cursor.png')
        pixmap = pixmap.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.cursor_new = QCursor(pixmap)
        QApplication.setOverrideCursor(QCursor(pixmap))
        

        #------- макет для меню -------#


        # макет кнопок
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.settings_button)
        button_layout.addWidget(self.exit_button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        # макет заголовка и картинки
        header_layout = QVBoxLayout()
        header_layout.addWidget(header)
        header_layout.addStretch()
        header_layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)
        header.setAlignment(Qt.AlignmentFlag.AlignTop)
        header_layout.setContentsMargins(30, 20, 40, 20)
        
        
        # главный макет
        parent_layout = QHBoxLayout()
        parent_layout.addLayout(button_layout)
        parent_layout.addLayout(header_layout)
        
        self.central_menu.setLayout(parent_layout)
        
        # CSS
        self.setStyleSheet('''
            QMainWindow {
                background-image: url('menu_background.png');
                background-position: center;
            }
            QLabel {
                color: #CF7A99;
                font-family: 'Game Paused DEMO';
                font-size: 38px;
            }
            QPushButton {
                font-family: 'ARCADECLASSIC';
                font-size: 30px;
                background-color: white;
                color: #963859;
                border: 2px solid #CF7A99;
                border-radius: 6px;
                padding: 6px 14px;
            }
                QPushButton:hover {
                background-color: #FAC3D2;
                border: #963859; 
            }
                QPushButton:pressed {
                background-color: #f48fb1;
                padding-top: 17px;
                padding-bottom: 13px;
            }
    ''')       
        
    def click_start(self):
        
        # Ещё CSS
        self.setObjectName('room_widget')
        self.setStyleSheet('''
            #room_widget {
            background-image: url("room_background.png");
            background-repeat: no-repeat;
            background-position: center;
            }
        ''')
        self.room = Room()
        self.room.button_back.clicked.connect(self.back_to_menu)
        self.setCentralWidget(self.room)
        

    def click_settings(self):
        print('Not implemented yet my b')

    
    def click_exit(self):
        QApplication.quit()

    
    def back_to_menu(self):
        self.setUpMainWindow()




