from PyQt5.QtWidgets import QApplication
import sys 
from mainwindow import MainWindow

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec( ) # executar