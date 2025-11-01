import random
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QLabel, QApplication

# ----- класс персонажа ----- #
class Teto(QLabel):
    def __init__(self, parent):
        super().__init__(parent)


        # спрайты
        self.idle_image = QPixmap('idle.png')
        self.dragging_image = QPixmap('drag.png')
        self.falling_image = QPixmap('fall.png')
        self.hit_floor_image = QPixmap('floor.png')
        self.pat_image = QPixmap('pat.png')

        self.setPixmap(self.idle_image)


        # флаги
        self.flag_fall = False
        self.flag_drag = False
        self.fell = False
        self.pat = False # флаг чтобы при нажатии ПКМ и ЛКМ/нажатии ПКМ во время выполнения другой функции не было багов
        
        
        # физика (сила тяжести постоянно увеличивает скорость падения)
        self.gravity = 0.5
        self.falling_speed = 0
        
        
        # SFX
        self.squeaky1_sfx = QSoundEffect()
        self.squeaky1_sfx.setSource(QUrl.fromLocalFile('snd_squeaky.wav'))
        self.squeaky2_sfx = QSoundEffect()
        self.squeaky2_sfx.setSource(QUrl.fromLocalFile('squeak_sfx.wav'))
        self.squeaky3_sfx = QSoundEffect()
        self.squeaky3_sfx.setSource(QUrl.fromLocalFile('squeaky_toy.wav'))


    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            if self.pat:
                self.stop_patting()

            # таймер чтобы функция falling проигрывалась много раз и Тето плавно падала
            self.timer_fall = QTimer()
            self.timer_fall.timeout.connect(self.falling)
            self.falling_speed = 0 # чтобы её можно было ловить в воздухе и она не разгонялась до скорость света
            self.flag_drag = True
            self.flag_fall = False
            self.timer_fall.stop()
            self.setPixmap(self.dragging_image)

        elif e.button() == Qt.MouseButton.RightButton:
            if not self.fell and not self.flag_fall and not self.flag_drag and not self.pat:
                self.patting()


    def mouseMoveEvent(self, event):
        if self.flag_drag and not self.pat:
            cursor_position = self.mapToParent(event.position())
            self.move(int(cursor_position.x() - 75), int(cursor_position.y() - 50)) # рандом числа чтобы курсор брал её за шкирку а не за край пнг


    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.flag_drag = False
            self.flag_fall = True
            self.setPixmap(self.falling_image)
            self.timer_fall.start(15)

        elif e.button() == Qt.MouseButton.RightButton:
            if self.pat:
                self.stop_patting()
                

    def patting(self):
        self.pat = True
        self.setPixmap(self.pat_image)
        pat_pixmap = QPixmap('cursor_petting.png')
        QApplication.setOverrideCursor(QCursor(pat_pixmap))
        
    
    def stop_patting(self):
        self.pat = False
        pixmap = QPixmap('cursor.png')
        pixmap = pixmap.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.cursor_new = QCursor(pixmap)
        QApplication.setOverrideCursor(QCursor(pixmap))
        self.setPixmap(self.idle_image)

            
    def falling(self):
        if self.flag_fall:
            self.falling_speed += self.gravity
            
            y = self.y() + self.falling_speed # скорость падения у
            x = self.x()
            self.floor = 280 # уровень пола по оси y
            self.right_wall = 380
            self.left_wall = 0.5
            self.ceiling = 50
            if y >= self.floor:
                y = self.floor
                self.flag_fall = False
                self.timer_fall.stop()
                self.falling_speed = 0
                self.setPixmap(self.hit_floor_image)
                random.choice([self.squeaky1_sfx, self.squeaky2_sfx, self.squeaky3_sfx]).play()
                self.fell = True
                self.timer_stand = QTimer()
                self.timer_stand.timeout.connect(self.standing_up)
                self.timer_stand.start(1000)

        if x > self.right_wall:
            x = self.right_wall

        if x < self.left_wall:
            x = self.left_wall

        self.move(int(x), int(y))


    def standing_up(self):
        if self.fell and not self.flag_drag and not self.flag_fall:
            self.timer_stand.stop()
            self.setPixmap(self.idle_image)
            self.move(self.x(), self.y() - 20) # чтобы вставшая Тето была на одном уровне с упавшим спрайтом
            self.fell = False


