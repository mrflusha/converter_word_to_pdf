import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStyle, QLabel, QMessageBox, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import pyqtSlot
import webbrowser
import func



import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)



class App(QDialog):




    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.title = 'One click one path .doc to .pdf'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 100
        #self.statusBar().showMessage('2022.')
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #39393c; color: white; font-size: 2em;")

        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)

        self.setLayout(windowLayout)


        self.setMinimumSize(600,400)
        self.setMaximumWidth(600)
        self.setMaximumHeight(400)

        
        self.show()
    

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 2)
        self.button = QPushButton('Convert .doc to .pdf')
        self.button_style = 'QPushButton {background-color: #308D46; color: #000; font-size: 18px; \
            border-width: 2px; border-style: solid; min-height: 30px; border-radius: 5px; margin-right:35%; border-color:white;}'
        self.button_style_pressed = 'QPushButton:clicked{background-color:grey; font-size: 18px;}'

        self.about = QPushButton('About')
        self.donate_style = 'QLineEdit{color:#308D46; font-size:16;}'
        self.vk_button = QPushButton("VK DONUT")
        self.vk_button.setStyleSheet('QPushButton{background-color:#000; color:#fff, font-style:VK-Sans}')


        self.doc_path_str = QLineEdit(self)
        self.pdf_path_str = QLineEdit(self)
        self.btc = QLineEdit(self)
        self.ccx = QLineEdit(self)
        self.doge = QLineEdit(self)
        self.xmr = QLineEdit(self)
        self.btc.setText("btc:35MWrX4QwJNYxA8p162aYhpsrPJ3BaZNMF")
        self.doge.setText('DE3b3gKoBj348qiKRXixLescNBhbjwnzF8')
        self.ccx.setText('ccx7bu2S15CF4jLCWyJAaGJPsGpZsh9Ud8xDeCo1pVocNuZG3JpbYnwXtznxBsofFP8JB32YYBmtwLdoEirjAbYo4DBZf7NbFS')
        self.xmr.setText('xmr:88fZ7HghwLi1aKHrcZXQCtTd7kEDHXxVBg1fk7Dibove8LJGMVZgUFbbip1LQ94VHmP1Cn2pNXx7K3M8ZWAau7PsSqt9DDy')
        self.btc.setStyleSheet('QLineEdit{color:red; background-color:black;}')
        self.btc.setReadOnly(True)
        self.doge.setReadOnly(True)
        self.ccx.setReadOnly(True)
        self.xmr.setReadOnly(True)

        self.doc_path_str.setStyleSheet(''' font-size: 18px; background-color:grey; color: white; ''')
        self.pdf_path_str.setStyleSheet(''' font-size: 18px;  background-color:grey; color: white; ''')
        self.doc_path_str.setPlaceholderText('Paste doc path')
        self.pdf_path_str.setPlaceholderText('Paste pdf path')
        self.button.setStyleSheet(self.button_style)

        self.about.setStyleSheet(self.button_style)
        self.doge.setStyleSheet(self.donate_style)
        self.btc.setStyleSheet(self.donate_style)
        self.ccx.setStyleSheet(self.donate_style)
        self.xmr.setStyleSheet(self.donate_style)
        self.ps = QLabel("For donations:")
        self.ps.setStyleSheet('''color:#308D46; font-size:22px; font-style: VK-Sans;''')

        #self.doge.setStyleSheet("QLineEdit[readOnly=\"true\"] {color: #808080; background-color: #F0F0F0; border: 1px solid #B0B0B0; border-radius: 2px;}")




        layout.addWidget(self.doc_path_str,0,0,1,2)
        layout.addWidget(self.pdf_path_str,1,0,1,2)
        layout.addWidget(self.button,2,1,1,2)
        layout.addWidget(QLabel("BTC:"),4,0)
        layout.addWidget(self.btc,4,1,1,2)
        layout.addWidget(QLabel("CCX:"),5,0)
        layout.addWidget(self.ccx,5,1,1,2)
        layout.addWidget(QLabel("DOGE:"),6,0)
        layout.addWidget(self.doge,6,1,1,2)
        layout.addWidget(QLabel("xmr:"),7,0)
        layout.addWidget(self.xmr,7,1,1,2)
        layout.addWidget(self.vk_button,8,1,1,2)
        layout.addWidget(self.about,9,0,1,1)

        layout.addWidget(self.ps,3,1)
        layout.setSpacing(10)
        


        self.horizontalGroupBox.setLayout(layout)
        self.button.clicked.connect(self.slot_method)
        self.about.clicked.connect(self.about_click)
        self.vk_button.clicked.connect(self.vk_don_click)


    @pyqtSlot()
    def slot_method(self):
        self.button.setStyleSheet(self.button_style_pressed)
        list_dir = [self.doc_path_str.text(),self.pdf_path_str.text()]


        if len(list_dir[0]) < 3 or len(list_dir[1]) < 3:
            self.click = QMessageBox.information(self, "Уведомление" , "\nPath to directory can't be empty\n" , QMessageBox.Ok)
        else:
            log = func.convert(list_dir[0],list_dir[1])
            func.del_temp(list_dir[1])
            self.click = QMessageBox.information(self, "Уведомление" , "\nLOG INFO:\n" + log , QMessageBox.Ok)

        if self.click == QMessageBox.Ok:
            self.button.setStyleSheet(self.button_style)

    def about_click(self):
        webbrowser.open('https://github.com/mrflusha/converter_word_to_pdf',new = 2)
    def vk_don_click(self):
        webbrowser.open("https://vk.com/public190359874?source=description&w=donut_payment-190359874", new = 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())