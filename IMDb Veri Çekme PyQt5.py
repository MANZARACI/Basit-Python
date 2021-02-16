# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from bs4 import BeautifulSoup
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 801, 431))
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 460, 361, 71))
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.film)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 460, 361, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.dizi)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addWidget(self.pushButton)
        h_box.addWidget(self.pushButton_2)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.plainTextEdit)
        v_box.addLayout(h_box)

        self.centralwidget.setLayout(v_box)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMDb En İyi Film/Dizi"))
        self.pushButton.setText(_translate("MainWindow", "En İyi 250 Film"))
        self.pushButton_2.setText(_translate("MainWindow", "En İyi 250 Dizi"))

    def film(self):
        url="https://www.imdb.com/chart/top"
        response=requests.get(url)
        içerik=response.content
        soup=BeautifulSoup(içerik,"html.parser")

        isimler=soup.find_all("td",{"class":"titleColumn"})
        puanlar=soup.find_all("td",{"class":"ratingColumn imdbRating"})

        with open("film aktar.txt","w",encoding="utf-8") as f:    
            
            for a,b in zip(isimler,puanlar):
                a=a.text
                a=a.strip()
                a=a.replace("\n","")

                b=b.text
                b=b.strip()
                b=b.replace("\n","")

                x=a+"  "+b+"\n*************************************************************************\n"

                f.write(x)

        with open("film aktar.txt","r",encoding="utf-8") as f:

            self.plainTextEdit.setPlainText(f.read())
    
    def dizi(self):
        url="https://www.imdb.com/chart/toptv"
        response=requests.get(url)
        içerik=response.content
        soup=BeautifulSoup(içerik,"html.parser")

        isimler=soup.find_all("td",{"class":"titleColumn"})
        puanlar=soup.find_all("td",{"class":"ratingColumn imdbRating"})

        with open("dizi aktar.txt","w",encoding="utf-8") as f:

            for a,b in zip(isimler,puanlar):
                a=a.text
                a=a.strip()
                a=a.replace("\n","")

                b=b.text
                b=b.strip()
                b=b.replace("\n","")

                x=a+"  "+b+"\n*************************************************************************\n"

                f.write(x)

        with open("dizi aktar.txt","r",encoding="utf_8") as f:
            self.plainTextEdit.setPlainText(f.read())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
