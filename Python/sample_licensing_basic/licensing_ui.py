import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QLineEdit
from uuid import getnode as get_mac
import hashlib
import uuid

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 900, 150)
        self.setWindowTitle('3DLynx Licensing Tool')
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(850, 20)
        self.textbox.setReadOnly(True)
        salt = uuid.uuid4().hex
        mac = str(get_mac())
        res = hashlib.sha256(salt.encode() + mac.encode()).hexdigest() + ':' + salt
        self.textbox.setText(res)
        self.show()


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())