from trackerApp import Ui_MainWindow

from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtGui import  QPixmap

from drawOnCropped import track
import pyrebase
from model import get_data,parse_data, get_coordinates
import time


# configNew = {
#     "apiKey": "AIzaSyBIFhbwdIXRf-TRlSvieuhw5VgnN4u9pp8",
#     "authDomain": "esp32data-e59a5.firebaseio.com",
#     "databaseURL": "https://esp32data-e59a5.firebaseio.com/",
#     "projectId": "esp32data-e59a5",
#     "storageBucket": "esp32data-e59a5.firebaseio.com",
# }

configNew = {
    "apiKey": "AIzaSyBNZHK027vpYHh5TXMzzjnAAWy5g3CZihw",
    "authDomain": "localization-9e689.firebaseio.com",
    "databaseURL": "https://localization-9e689.firebaseio.com/",
    "projectId": "localization-9e689",
    "storageBucket": "localization-9e689.firebaseio.com",
}

#  apiKey: "AIzaSyBNZHK027vpYHh5TXMzzjnAAWy5g3CZihw",
#     authDomain: "localization-9e689.firebaseapp.com",
#     databaseURL: "https://l...content-available-to-author-only...o.com",
#     projectId: "localization-9e689",
    # storageBucket: "localization-9e689.appspot.com",
#     messagingSenderId: "1095700650219",
#     appId: "1:1095700650219:web:8cd6a6323cabf0f6be46ae",
#     measurementId: "G-PQPC79W9XK"



class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = self.ui.label
        
        self.firebase = pyrebase.initialize_app(configNew)
        self.db = self.firebase.database()
        self.idx = 0

        self.initImg = "dFloorMapEdited.jpg"
        self.modImg = "modified.png"
        
        self.refreshView(self.initImg)


    def refreshView(self,img):
        self.view.clear()   
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToWidth(512)
        pixmap = pixmap.scaledToHeight(512)
        self.view.setPixmap(pixmap)


    def start_loop(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.start_tracking)
        timer.start(10)



    def start_tracking(self):
        self.idx += 0.2 if (self.idx <= 10) else 0
        # time.sleep(0.005)
       
        data = get_data(self.firebase)
        print(f'data : {data}')
       
        rss_list = parse_data(data)
        print(f'rss_list : {rss_list}')

        # print(rss_list)
        self.predictedClass = get_coordinates(rss_list) # TO BE USED Later
        self.predictedClass = 13
        self.db.child("coordinates/y").set(int(self.predictedClass)) # Push predictions to the cloud
        # print(self.yCoordinates)
        
        
        # coords = mapCoordinates(1426,5700-264*self.yCoordinates,img)   # TODO Uncomment
        
        
        # print(self.predictedClass) 
        drawnCircleRad = 12
        track(self.predictedClass,self.initImg,self.modImg,drawnCircleRad)
        self.refreshView(self.modImg)





def main():
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.ui.pushButton.clicked.connect(application.start_loop)

    application.show()
    app.exec_()


if __name__ == "__main__":
    main()