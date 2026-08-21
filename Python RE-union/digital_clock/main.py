import datetime, time
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout,QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QTimer, QTime, Qt
print(time.localtime().tm_hour)

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "mixkit-rooster-crowing-in-the-morning-2462.wav"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)
    
class DigitalClock(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        #self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 300, 400, 200) # (x, y, width, height)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;" "font-family: Arial;" "color: green;")
        self.setStyleSheet("background-color: black;")
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
    
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
    main()