#!/usr/bin/env python

import itk
import sys
import vtk
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(Qt.QMainWindow):

    def __init__(self, parent = None):
        Qt.QMainWindow.__init__(self, parent)

        self.frame = Qt.QFrame()
        self.vl = Qt.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)

        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.im = itk.imread('/home/francois.budin/data/Slicer/MRHead_f.nrrd')
        self.viewer = itk.ViewImage.New(self.im, RenderWindowInteractor=self.iren)
        self.viewer.Update()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)

        self.show()

        #self.button = QtGui.QPushButton('Exit', self)
        #self.button.clicked.connect(self.exit_button)
        #self.vl.addWidget(self.button)

    def exit_button(self):
        print("exit")
        sys.exit(0)

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
