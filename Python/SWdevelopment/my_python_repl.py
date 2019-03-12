import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import subprocess
import sys


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("my_python_ui.ui")
        self.ui.Input_line.editingFinished.connect(self.proceed)
        self.ui.show()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.key_Enter:
            self.proceed()
            
    def changeOutput(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.proceed()

    def proceed(self):
        proc = subprocess.Popen("""python -c """ + "%s > c:\\res.txt" % self.ui.Input_line.text(), stdout = subprocess.PIPE)
        output = proc.stdout.read().decode('ascii')
        self.ui.Output_area.setText(">> "+output)
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
    
"""
# PyQt basic tutorial
https://opentutorials.org/module/544/9494

# name of Enter key
https://stackoverflow.com/questions/38507011/implementing-keypressevent-in-qwidget

# set Text (change label text)
https://stackoverflow.com/questions/19985640/change-qlabel-text-dynamically-in-pyqt4

# read Text
https://stackoverflow.com/questions/3016974/how-to-get-text-in-qlineedit-when-qpushbutton-is-pressed-in-a-string

# editing Finished
https://www.tutorialspoint.com/pyqt/pyqt_qlineedit_widget.htm

# button clicked connect
https://www.pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/

"""

"""
임시 저장용 코드

while True:
  print(">>> ", end='')
  cmd = input()
  proc = subprocess.Popen("""'python -c' """ + "%s" % cmd, stdout=subprocess.PIPE)
  output = proc.stdout.read()
  print(output)


#self.ui.Input_line.keyPressed.connect(self.changeOutput)

"""
