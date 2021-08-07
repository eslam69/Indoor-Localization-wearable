import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from draw import mapCoordinates, drawCircle
import pyrebase
from model import get_data, parse_data, get_coordinates
import time

configNew = {
    "apiKey": "AIzaSyBIFhbwdIXRf-TRlSvieuhw5VgnN4u9pp8",
    "authDomain": "esp32data-e59a5.firebaseio.com",
    "databaseURL": "https://esp32data-e59a5.firebaseio.com/",
    "projectId": "esp32data-e59a5",
    "storageBucket": "esp32data-e59a5.firebaseio.com",
}

img = "departmentFloorMap.png"
saved = "modified.png"


class MainWindow(QMainWindow):
    idx = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "SBME Localizer"
        self.setWindowTitle(self.title)
        self.main_widget = QWidget(self)
        self.init_map()
        self.setCentralWidget(self.main_widget)
        self.firebase = pyrebase.initialize_app(configNew)
        self.db = self.firebase.database()
        self.idx = 0
        self.button.clicked.connect(self.start_loop)

        self.show()

    def start_loop(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.start_tracking)
        timer.start(150)

    def init_map(self):
        self.layout = QVBoxLayout(self.main_widget)
        self.label = QLabel(self)
        pixmap = QPixmap('departmentFloorMap.png')
        self.button = QPushButton("Start", self)
        self.label.setPixmap(pixmap)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        # self.setCentralWidget(self.label,self.button)
        # self.resize(self.pixmap.width(), self.pixmap.height()+10)
        # self.setFixedSize(self.pixmap.width(), self.pixmap.height()+10)

    def start_tracking(self):
        self.idx += 1.2
        # time.sleep(0.5)
        # Down Hallway starts at (1426,3054)
        data = get_data(self.firebase)
        rss_list = parse_data(data)
        print(rss_list)
        self.Coordinates = get_coordinates(rss_list)  # TO BE USED Later

        # TODO map coordinates to scale
        if self.Coordinates == 0:
            print("in hall 0")
            coords = (1470, 5304)
        elif self.Coordinates == 1:
            print("in hall 1")
            coords = (1470, 4908)

        elif self.Coordinates == 2:
            print("in hall 2")
            coords = (1470, 4100)
        elif self.Coordinates == 3:
            print("in hall 3")
            coords = (1470, 3000)

        elif self.Coordinates == 4:
            print("in TA ROOM")
            coords = (1100, 3200)
        elif self.Coordinates == 5:
            print("in the Lab")
            coords = (900, 4350)

        # Push predictions to the cloud
        self.db.child("coordinates").child("x").set(
            coords[0])
        self.db.child("coordinates").child("y").set(
            coords[1])

        print("Place Prediction: ", self.Coordinates)
        coords = mapCoordinates(coords[0], coords[1], img)
        drawCircle(img, 7, coords, saved)
        pixmap = QPixmap('modified.png')
        self.label.setPixmap(pixmap)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    app.setWindowIcon(QIcon('resources/logoMap.png'))
    w = MainWindow()
    # w.show()
    sys.exit(app.exec_())
