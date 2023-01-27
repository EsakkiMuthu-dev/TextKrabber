from PyQt5.QtWidgets import *
from PyQt5 import uic

class gui(QMainWindow):
    def __init__(self) -> None:
        super(gui,self).__init__()
        uic.loadUi("./UI/Login.ui",self)
        self.show()
        self.loginbtn.clicked.connect(self.login)
        self.msgbtn.clicked.connect(lambda:self.sayit(self.textbox.toPlainText()))
        self.actionClose.triggered.connect(exit)
    def login(self):
        if self.uname.text()=="muthu" and self.passwd.text() == "maha":
            self.textbox.setEnabled(True)
            self.msgbtn.setEnabled(True)
        else:
            alert=QMessageBox()
            alert.setText("Enter correct password and user name")
            alert.exec_()
    def sayit(self,msg):
        m=QMessageBox()
        m.setText(msg)
        m.exec_()

def main():
    app=QApplication([])
    window=gui()
    app.exec_()
    # app =QApplication([])
    # window=QWidget()
    # window.setGeometry(170,100,300,300)
    # window.setWindowTitle("My Gui")
    
    # layout=QVBoxLayout()
    # label=QLabel("Press the button below !!")
    # textbox=QTextEdit()
    # button=QPushButton("Press Me!")
    # button.clicked.connect(lambda:onclick(textbox.toPlainText()))


    # layout.addWidget(label)
    # layout.addWidget(textbox)
    # layout.addWidget(button)

    # window.setLayout(layout)

    # label=QLabel(window)
    # label.setText("Hello From Qt")
    # label.move(50,100)
    # label.setFont(QFont("Noto sans",17))

    # window.show()
    # app.exec_()

def onclick(txt):
    msg=QMessageBox()
    msg.setText(txt)
    msg.exec_()

if __name__ == "__main__":
    main()