# INTRO 
'''import sys # system specific parameters and functions. Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. always available
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
'''



# LABLES 
'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt # Qt class is used for alignment

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        label = QLabel("HEY", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 700, 700)
        label.setStyleSheet("color: grey;" "background-color: black;" "font-weight: bold;" "font-style: italic;" "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop) # Vertically Top
        #label.setAlignment(Qt.AlignBottom)  # Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter) # Vertically Center
        #label.setAlignment(Qt.AlignRight)   # Horizontally Right
        #label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        #label.setAlignment(Qt.AlignLeft)    # Horizontally Left
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)    # Center & Top, | ALLOWS TO combine

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()'''



# IMAGES
'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap # QPixmap is used for handling images & provides functionality for loding, manipulating, & displaying images. 

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)
        pixmap = QPixmap("PyQt5/gui.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        #label.setGeometry(self.width() - label.width(), self.height() - label.height(), label.width(), label.height()) # bottom right corner
        #label.setGeometry(0 , self.height() - label.height(), label.width(), label.height()) # bottom left corner
        #label.setGeometry((self.width() - label.width()) // 2, self.height() - label.height(), label.width(), label.height()) # bottom center
        #label.setGeometry(self.width() - label.width(), (self.height() - label.height()) //2, label.width(), label.height()) # right center
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) //2, label.width(), label.height()) # center

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()'''


# LAYOUTS
'''import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("1", self)
        label2 = QLabel("2", self)
        label3 = QLabel("3", self)
        label1.setStyleSheet("background-color: pink")
        label2.setStyleSheet("background-color: red")
        label3.setStyleSheet("background-color: blue")
        #vbox = QVBoxLayout() # vertical layout
        #hbox = QHBoxLayout() # horizontal layout
        grid = QGridLayout() # Grid layout
        grid.addWidget(label1, 0, 0) # (layout, row, coloumn)
        grid.addWidget(label2, 1, 1)
        grid.addWidget(label3, 2, 2)
        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()'''


# BUTTONS
'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hey", self)
        self.initUI()
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # signal.connect(slot)
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")
    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked")
        self.label.setText("Bye")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()'''


# CHECKBOXES
'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt # This module of QtCore contains non-Gui classes relevant to PyQt5 applications

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.checkbox = QCheckBox("DEAD TODAY?", self)
        self.initUI()
    def initUI(self):
        self.checkbox.setGeometry(20, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_change)
    def checkbox_change(self, state):
        if state == Qt.Checked:
            print("Dead")
        else:
            print("Not Dead")

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
'''


# RADIO BUTTONS (limited to just one option)
'''import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("Offline", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        self.setStyleSheet("QRadioButton{" "font-size: 40px;" "font-family: Arial;" "padding: 10px"
        "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.radio1.toggled.connect(self.radioButtonChange)
        self.radio2.toggled.connect(self.radioButtonChange)
        self.radio3.toggled.connect(self.radioButtonChange)
        self.radio4.toggled.connect(self.radioButtonChange)
        self.radio5.toggled.connect(self.radioButtonChange)
    def radioButtonChange(self):
        radioButton = self.sender() # sender method is going to return the widget that was clicked or that sent the signal
        if radioButton.isChecked():
            print(f"{radioButton.text()} is selected")

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()'''


# LINE EDITS OR TEXT BOXES
'''import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setGeometry(700, 300, 700, 700) # (x, y, widht, height)
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.lineEdit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()
    def initUI(self):
        self.lineEdit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(220, 10, 100, 40)
        self.lineEdit.setStyleSheet("font-size: 25px;" "font-family: Arial;")
        self.button.setStyleSheet("font-size: 15px;" "font-family: Arial;")
        self.lineEdit.setPlaceholderText("Enter Your Name")
        self.button.clicked.connect(self.sumbit)
    def sumbit(self):
        text = self.lineEdit.text()
        print(f"Hey {text}")

def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()'''


# CSS STYLES
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("What IS THIS GUI")
        self.setWindowIcon(QIcon("PyQt5/gui.png"))
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            font-family: Arial;
            padding: 15px 75px ;   
            margin: 25px;
            border: 3px solid;   
            border-radius: 15px;
            }    
        QPushButton#button1{
            background-color: hsl(192, 4%, 59%)           
            }
        QPushButton#button2{
            background-color: hsl(192, 49%, 69%)          
            }
        QPushButton#button3{
            background-color: hsl(336, 62%, 71%)           
            }
        QPushButton#button1:hover{
            background-color: hsl(192, 4%, 79%)            
            }
        QPushButton#button2:hover{
            background-color: hsl(192, 49%, 89%)             
            }
        QPushButton#button3:hover{
            background-color: hsl(336, 62%, 91%)           
            }
""")
def main():
    app = QApplication(sys.argv) # sys.argv this allows PyQt5 to process any command line arguments intended for it, that if we use command prompt or terminal
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()