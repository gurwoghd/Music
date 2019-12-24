import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from playsound import *

form_class = uic.loadUiType("C:\\Users\\PC\\Documents\\Music\\music_player.ui")[0]
class myApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.isPaused = False # 일시정지 되었는가?

        self.past_button.clicked.connect(self.playPastMusic)
        self.next_button.clicked.connect(self.playNextMusic)
        self.pause_button.clicked.connect(self.PauseMusic)
        self.AddSong.clicked.connect(self.addSong)

    def playPastMusic(self): # 이전 음악을 재생
        print('past music!')

    def playNextMusic(self): # 다음 음악을 재생
        print('next music!')

    def PauseMusic(self): # 현재 음악을 pause/unpause
        if not self.isPaused:
            print('pause music!')
            self.pause_button.setText('재생')
        else:
            print('unpause music!')
            self.pause_button.setText('일시정지')
        self.isPaused = not self.isPaused
    
    def addSong(self): # 음악을 추가
        pass

app = QApplication(sys.argv)
mainwindow = myApp()
mainwindow.show()
app.exec_()