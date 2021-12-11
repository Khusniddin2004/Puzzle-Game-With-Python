from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class Tugma(QPushButton):
    def click(self,func):
        self.clicked.connect(func)
class Winfow(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
    def font(self):
        # self.setFont(QFont("Times",40))
        pass
    def start(self):
        self.finish = QMessageBox(self)
        self.lab=QLabel(self)
        self.lab.setFont(QFont("Times",20))
        self.lab.move(300,300)
        self.A=['X','O']
        self.a=0
        self.X=QRadioButton("X",self)
        self.X.setFont(QFont("Times",20))
        self.X.move(50,50)

        self.o=QRadioButton("O",self)
        self.o.setFont(QFont("Times",20))
        self.o.move(50,110)

        self.goo=QPushButton("Go",self)
        self.goo.setFont(QFont("Times",20))
        self.goo.move(40,150)
        self.goo.clicked.connect(self.go)

        self.a1=Tugma("1",self)
        self.a1.setFont(QFont("Times",20))
        self.a1.setGeometry(100,50,50,50)

        self.a2=Tugma("2",self)
        self.a2.setFont(QFont("Times",20))
        self.a2.setGeometry(150,50,50,50)

        self.a3=Tugma("3",self)
        self.a3.setFont(QFont("Times",20))
        self.a3.setGeometry(200,50,50,50)

        self.a4=Tugma("4",self)
        self.a4.setFont(QFont("Times",20))
        self.a4.setGeometry(100,100,50,50)

        self.a5=Tugma("5",self)
        self.a5.setFont(QFont("Times",20))
        self.a5.setGeometry(150,100,50,50)

        self.a6=Tugma("6",self)
        self.a6.setFont(QFont("Times",20))
        self.a6.setGeometry(200,100,50,50)

        self.a7=Tugma("7",self)
        self.a7.setFont(QFont("Times",20))
        self.a7.setGeometry(100,150,50,50)

        self.a8=Tugma("8",self)
        self.a8.setFont(QFont("Times",20))
        self.a8.setGeometry(150,150,50,50)

        self.a9=Tugma("9",self)
        self.a9.setFont(QFont("Times",20))
        self.a9.setGeometry(200,150,50,50)

        
        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)
        self.a7.click(self.A7)
        self.a8.click(self.A8)
        self.a9.click(self.A9)
    
    def chec(self,pac):
        if self.a==1:
                pac.setText('X')
                self.a=0
                self.XX()
        else:
            pac.setText('O')
            self.a=1
            self.O()
    def go(self):
        if self.X.isChecked():
            self.a=1
        else:
            self.a=0
        self.X.close()
        self.o.close()
        self.goo.close()
    def A1(self):
        if self.a1.text()=='1':
            self.chec(self.a1)
    def A2(self):
        if self.a2.text()=='2':
            self.chec(self.a2)
    def A3(self):
        if self.a3.text()=='3':
            self.chec(self.a3)
    def A4(self):
        if self.a4.text()=='4':
            self.chec(self.a4)
    def A5(self):
        if self.a5.text()=='5':
            self.chec(self.a5)
    def A6(self):
        if self.a6.text()=='6':
            self.chec(self.a6)
    def A7(self):
        if self.a7.text()=='7':
            self.chec(self.a7)
    def A8(self):
        if self.a8.text()=='8':
            self.chec(self.a8)
    def A9(self):
        if self.a9.text()=='9':
            self.chec(self.a9)

    def O(self):
        if (self.a1.text()==self.a2.text() and self.a1.text()==self.a3.text()) or (self.a1.text()==self.a4.text() and self.a1.text()==self.a7.text()) or (self.a1.text()==self.a5.text() and self.a1.text()==self.a9.text()) or (self.a2.text()==self.a5.text() and self.a2.text()==self.a8.text()) or (self.a3.text()==self.a6.text() and self.a3.text()==self.a9.text()) or (self.a4.text()==self.a5.text() and self.a4.text()==self.a6.text()) or (self.a7.text()==self.a8.text() and self.a7.text()==self.a9.text()):
            self.finish.setWindowTitle("yutish")
            self.finish.setText("O yutdi")
            self.finish.exec_()
    def XX(self):
        if (self.a1.text()==self.a2.text() and self.a1.text()==self.a3.text()) or (self.a1.text()==self.a4.text() and self.a1.text()==self.a7.text()) or (self.a1.text()==self.a5.text() and self.a1.text()==self.a9.text()) or (self.a2.text()==self.a5.text() and self.a2.text()==self.a8.text()) or (self.a3.text()==self.a6.text() and self.a3.text()==self.a9.text()) or (self.a4.text()==self.a5.text() and self.a4.text()==self.a6.text()) or (self.a7.text()==self.a8.text() and self.a7.text()==self.a9.text()):
            self.finish.setWindowTitle("Yutish")
            self.finish.setText("x yutdi")
            self.finish.exec_()
app = QApplication(sys.argv)
oyna=Winfow()
oyna.show()
sys.exit(app.exec_())