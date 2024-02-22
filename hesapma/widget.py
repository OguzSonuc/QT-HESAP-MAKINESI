# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.s0.clicked.connect(self.sayi0)
        self.ui.s1.clicked.connect(self.sayi1)
        self.ui.s2.clicked.connect(self.sayi2)
        self.ui.s3.clicked.connect(self.sayi3)
        self.ui.s4.clicked.connect(self.sayi4)
        self.ui.s5.clicked.connect(self.sayi5)
        self.ui.s6.clicked.connect(self.sayi6)
        self.ui.s7.clicked.connect(self.sayi7)
        self.ui.s8.clicked.connect(self.sayi8)
        self.ui.s9.clicked.connect(self.sayi9)
        self.ui.toplama.clicked.connect(self.toplama)
        self.ui.cikarma.clicked.connect(self.cikarma)
        self.ui.carpma.clicked.connect(self.carpma)
        self.ui.bolme.clicked.connect(self.bolme)
        self.ui.esittir.clicked.connect(self.esittir)
        self.ui.temizle.clicked.connect(self.temizle)
        self.ui.yuzde.clicked.connect(self.yuzde)
        self.ui.silme.clicked.connect(self.silme)
        

    def sayi0(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"0")
    def sayi1(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"1")
    def sayi2(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"2")
    def sayi3(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"3")
    def sayi4(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"4")
    def sayi5(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"5")
    def sayi6(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"6")
    def sayi7(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"7")
    def sayi8(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"8")
    def sayi9(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"9")
    def toplama(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"+")
    def cikarma(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"-")
    def carpma(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"*")
    def bolme(self):
        self.ui.sonuc.setText(self.ui.sonuc.text()+"/")
    def esittir(self):
        s = eval(self.ui.sonuc.text())
        self.ui.sonuc.setText(str(s))
    def temizle(self):
        self.ui.sonuc.clear()
    def yuzde(self):
        sayi=float(self.ui.sonuc.text())
        sonuc = (sayi / 100)
        self.ui.sonuc.setText(format(sonuc,"15"))
    def silme(self):
        text = self.ui.sonuc.text()
        self.ui.sonuc.setText(text[:len(text)-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
