from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont
import sys
# check class
class Button(QPushButton):
    def __init__(self,bosh=list(),btn=list()):    
        if ((bosh[0]-btn[0] == 40 and bosh[1]-btn[1] == 0) or (bosh[0]-btn[0] == 0 and bosh[1]-btn[1] == 40)) or ((btn[0]-bosh[0] == 40 and btn[1]-bosh[1] == 0) or (btn[0]-bosh[0] == 0 and btn[1]-bosh[1] == 40)):
            btn[0],btn[1],bosh[0],bosh[1]=bosh[0],bosh[1],btn[0],btn[1]
        elif ((bosh[0]-btn[0] == 30 and bosh[1]-btn[1] == 0) or (bosh[0]-btn[0] == 0 and bosh[1]-btn[1] == 30)) or ((btn[0]-bosh[0] == 30 and btn[1]-bosh[1] == 0) or (btn[0]-bosh[0] == 0 and btn[1]-bosh[1] == 30)):
            btn[0],btn[1],bosh[0],bosh[1]=bosh[0],bosh[1],btn[0],btn[1]

# main class
class Mini_game(QWidget):
    # main method
    def __init__(self):
        super().__init__()
        self.start()
    # run game method
    def start(self):
        # geometries
        self.finish = QMessageBox(self)
        self.butn1 = [20,20]
        self.butn2 = [20,50]
        self.butn3 = [60,50]
        self.butn4 = [60,20]
        self.butn5 = [100,20]
        self.butn6 = [20,80]
        self.butn7 = [100,110]
        self.butn8 = [100,50]
        self.butn9 = [20,140]
        self.butn10 = [20,110]
        self.butn11 = [60,110]
        self.butn12 = [60,80]
        self.butn13 = [100,80]
        self.butn14 = [60,140]
        self.bosh_joy = [100,140]
        # buttons
        self.btn1 = QPushButton("1",self)
        self.btn1.setFont(QFont("Times",20))
        self.btn1.setGeometry(self.butn1[0],self.butn1[1],50,36)
        self.btn1.clicked.connect(self.tugma_1)

        self.btn2 = QPushButton("2",self)
        self.btn2.setFont(QFont("Times",20))
        self.btn2.setGeometry(self.butn2[0],self.butn2[1],50,36)
        self.btn2.clicked.connect(self.tugma_2)

        self.btn3 = QPushButton("3",self)
        self.btn3.setFont(QFont("Times",20))
        self.btn3.setGeometry(self.butn3[0],self.butn3[1],50,36)
        self.btn3.clicked.connect(self.tugma_3)

        self.btn4 = QPushButton("4",self)
        self.btn4.setFont(QFont("Times",20))
        self.btn4.setGeometry(self.butn4[0],self.butn4[1],50,36)
        self.btn4.clicked.connect(self.tugma_4)

        self.btn5 = QPushButton("5",self)
        self.btn5.setFont(QFont("Times",20))
        self.btn5.move(self.butn5[0],self.butn5[1])
        self.btn5.clicked.connect(self.tugma_5)

        self.btn6 = QPushButton("6",self)
        self.btn6.setFont(QFont("Times",20))
        self.btn6.setGeometry(self.butn6[0],self.butn6[1],50,36)
        self.btn6.clicked.connect(self.tugma_6)

        self.btn7 = QPushButton("7",self)
        self.btn7.setFont(QFont("Times",20))
        self.btn7.setGeometry(self.butn7[0],self.butn7[1],50,36)
        self.btn7.clicked.connect(self.tugma_7)

        self.btn8 = QPushButton("8",self)
        self.btn8.setFont(QFont("Times",20))
        self.btn8.setGeometry(self.butn8[0],self.butn8[1],50,36)
        self.btn8.clicked.connect(self.tugma_8)

        self.btn9 = QPushButton("9",self)
        self.btn9.setFont(QFont("Times",20))
        self.btn9.setGeometry(self.butn9[0],self.butn9[1],50,36)
        self.btn9.clicked.connect(self.tugma_9)

        self.btn10 = QPushButton("10",self)
        self.btn10.setFont(QFont("Times",20))
        self.btn10.setGeometry(self.butn10[0],self.butn10[1],50,36)
        self.btn10.clicked.connect(self.tugma_10)

        self.btn11 = QPushButton("11",self)
        self.btn11.setFont(QFont("Times",20))
        self.btn11.setGeometry(self.butn11[0],self.butn11[1],50,36)
        self.btn11.clicked.connect(self.tugma_11)

        self.btn12 = QPushButton("12",self)
        self.btn12.setFont(QFont("Times",20))
        self.btn12.setGeometry(self.butn12[0],self.butn12[1],50,36)
        self.btn12.clicked.connect(self.tugma_12)

        self.btn13 = QPushButton("13",self)
        self.btn13.setFont(QFont("Times",20))
        self.btn13.setGeometry(self.butn13[0],self.butn13[1],50,36)
        self.btn13.clicked.connect(self.tugma_13)

        self.btn14 = QPushButton("14",self)
        self.btn14.setFont(QFont("Times",20))
        self.btn14.setGeometry(self.butn14[0],self.butn14[1],50,36)
        self.btn14.clicked.connect(self.tugma_14)
    # show message
    def fin(self):
        if (self.butn1[0]==20 and self.butn1[1]==20) and (self.butn2[0]==60 and self.butn2[1]==20) and (self.butn3[0]==100 and self.butn3[1]==20) and (self.butn4[0]==20 and self.butn4[1]==50) and (self.butn5[0]==60 and self.butn5[1]==50) and (self.butn6[0]==100 and self.butn6[1]==50) and (self.butn7[0]==20 and self.butn7[1]==80) and (self.butn8[0]==60 and self.butn8[1]==80) and (self.butn9[0]==100 and self.butn9[1]==80) and (self.butn10[0]==20 and self.butn10[1]==110) and (self.butn11[0]==60 and self.butn11[1]==110) and (self.butn12[0]==100 and self.butn12[1]==110) and (self.butn13[0]==20 and self.butn13[1]==140) and (self.butn14[0]==60 and self.butn14[1]==140):
            self.finish.setWindowTitle("Finish!")
            self.finish.setText("Tabriklaymiz siz yutdingiz!")
            self.finish.exec_()
    # clic button
    def tugma_1(self):
        Button(self.bosh_joy,self.butn1)
        self.btn1.move(self.butn1[0],self.butn1[1])
        self.fin()
    def tugma_2(self):
        Button(self.bosh_joy,self.butn2)
        self.btn2.move(self.butn2[0],self.butn2[1])
        self.fin()
    def tugma_3(self):
        Button(self.bosh_joy,self.butn3)
        self.btn3.move(self.butn3[0],self.butn3[1])
        self.fin()
    def tugma_4(self):
        Button(self.bosh_joy,self.butn4)
        self.btn4.move(self.butn4[0],self.butn4[1])
        self.fin()
    def tugma_5(self):
        Button(self.bosh_joy,self.butn5)
        self.btn5.move(self.butn5[0],self.butn5[1])
        self.fin()
    def tugma_6(self):
        Button(self.bosh_joy,self.butn6)
        self.btn6.move(self.butn6[0],self.butn6[1])
        self.fin()
    def tugma_7(self):
        Button(self.bosh_joy,self.butn7)
        self.btn7.move(self.butn7[0],self.butn7[1])
        self.fin()
    def tugma_8(self):
        Button(self.bosh_joy,self.butn8)
        self.btn8.move(self.butn8[0],self.butn8[1])
        self.fin()
    def tugma_9(self):
        Button(self.bosh_joy,self.butn9)
        self.btn9.move(self.butn9[0],self.butn9[1])
        self.fin()
    def tugma_10(self):
        Button(self.bosh_joy,self.butn10)
        self.btn10.move(self.butn10[0],self.butn10[1])
        self.fin()
    def tugma_11(self):
        Button(self.bosh_joy,self.butn11)
        self.btn11.move(self.butn11[0],self.butn11[1])
        self.fin()
    def tugma_12(self):
        Button(self.bosh_joy,self.butn12)
        self.btn12.move(self.butn12[0],self.butn12[1])
        self.fin()
    def tugma_13(self):
        Button(self.bosh_joy,self.butn13)
        self.btn13.move(self.butn13[0],self.butn13[1])
        self.fin()
    def tugma_14(self):
        Button(self.bosh_joy,self.butn14)
        self.btn14.move(self.butn14[0],self.butn14[1])
        self.fin()
app = QApplication(sys.argv)
window = Mini_game()
window.setGeometry(100,100,200,200)
window.show()
sys.exit(app.exec_())

