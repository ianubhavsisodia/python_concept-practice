from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("HEllo World!", self)
        btn.move(50,75)
        self.setGeometry(100,100,200,150)
        self.setWindowTitle("PyQt Window")
        self.show()

if __name__ == "__main__":
    app=QApplication(sys.argv) #creating an instance of the application class
    win=Window() #creating a new object from our defined class and passing it to the variable
    sys.exit(app.exec_())