import sys
from PyQt4 import QtCore, QtGui, uic

w = uic.loadUiType("servidor.ui")[0]

class VentanaServidor(QtGui.QWidget, w):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

app = QtGui.QApplication(sys.argv)
MiVentana = VentanaServidor(None)
MiVentana.show()
app.exec_()