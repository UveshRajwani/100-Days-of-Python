import os
import sys

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.gototext)
        self.pushButton_2.clicked.connect(self.gotoimg)
        self.pushButton_3.clicked.connect(self.gotoimgandtext)

    def gototext(self):
        text = TextScreen()
        widget.addWidget(text)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoimg(self):
        img = imageScreen()
        widget.addWidget(img)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoimgandtext(self):
        imgandtext = imageandtextScreen()
        widget.addWidget(imgandtext)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TextScreen(QDialog):
    def __init__(self):
        super(TextScreen, self).__init__()
        loadUi("login.ui", self)
        self.pushButton.clicked.connect(self.addtext)
        self.watermark = ''
        self.pushButton_2.clicked.connect(self.save)

    def addtext(self):
        file_filter = 'image File (*.jpg *.png);;'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='image File (*.jpg *.png)'
        )
        image = Image.open(response[0])
        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)
        font = ImageFont.truetype("arial.ttf", 50)
        draw.text((0, 0), self.lineEdit.text(), (255, 255, 255), font=font)
        plt.subplot(1, 2, 1)
        self.watermark = watermark_image
        print(response[0])

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        watermark_image = self.watermark
        watermark_image.save(filePath)
        watermark_image.show()

        plt.imshow(watermark_image)


class imageScreen(QDialog):
    def __init__(self):
        super(imageScreen, self).__init__()
        loadUi("img.ui", self)
        self.base_img = ''
        self.pushButton.clicked.connect(self.get_base_image)
        self.pushButton_2.clicked.connect(self.add_water_mark)
        self.complete_img = ''
        self.pushButton_3.clicked.connect(self.save)

    def get_base_image(self):
        file_filter = 'image File (*.jpg *.png);;'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='image File (*.jpg *.png)'
        )
        image = Image.open(response[0])
        self.base_img = image.copy()

    def add_water_mark(self):
        file_filter = 'image File (*.jpg *.png);;'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='image File (*.jpg *.png)'
        )
        watermark_image = Image.open(response[0])
        size = (500, 100)
        watermark_image.thumbnail(size)
        image = self.base_img
        image.paste(watermark_image, (500, 200))
        self.complete_img = image.copy()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        watermark_image = self.complete_img
        watermark_image.save(filePath)
        watermark_image.show()

        plt.imshow(watermark_image)


class imageandtextScreen(QDialog):
    def __init__(self):
        super(imageandtextScreen, self).__init__()
        loadUi("textandimg.ui", self)
        self.base_img = ''
        self.pushButton.clicked.connect(self.get_base_image)
        self.pushButton_2.clicked.connect(self.add_water_mark)
        self.complete_img = ''
        self.pushButton_3.clicked.connect(self.save)

    def get_base_image(self):
        file_filter = 'image File (*.jpg *.png);;'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='image File (*.jpg *.png)'
        )
        image = Image.open(response[0])
        self.base_img = image.copy()

    def add_water_mark(self):
        file_filter = 'image File (*.jpg *.png);;'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='image File (*.jpg *.png)'
        )
        watermark_image = Image.open(response[0])
        size = (500, 100)
        watermark_image.thumbnail(size)
        image = self.base_img
        image.paste(watermark_image, (500, 200))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 50)
        draw.text((0, 0), self.lineEdit.text(), (255, 255, 255), font=font)
        plt.subplot(1, 2, 1)
        self.complete_img = image.copy()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        watermark_image = self.complete_img
        watermark_image.save(filePath)
        watermark_image.show()

        plt.imshow(watermark_image)


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
