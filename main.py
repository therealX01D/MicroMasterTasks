# This Python file uses the following encoding: utf-8
import sys
from lexicalana import *
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QMessageBox
    )
from PySide6.QtCore import QRegularExpression,Qt
from PySide6.QtGui import QRegularExpressionValidator
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
"""
this is the code for the main page and the only page to be concise 
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Draw Plot")
        self.hlay = QHBoxLayout()
        self.vlay = QVBoxLayout()
        self.labl1 = QLabel("Expression")
        self.labl1.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.labl2 = QLabel("Minimum")
        self.labl2.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.labl3 = QLabel("Maximum")
        self.labl3.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.EXP = QLineEdit()
        self.MIN = QLineEdit()
        self.MAX = QLineEdit()

        #rx = QRegularExpression("([-+]?((((([0-9]*\.?[0-9]+)|x)[\/\+\-\*\^])+([-+]?(([0-9]*\.?[0-9]+)|x)))|x|[0-9]*))")
        #validator = QRegularExpressionValidator(rx, self)
        #self.inpu.setValidator(validator)
        self.button = QPushButton("Draw Expression")
        self.button.clicked.connect(self.clickHandle)
        self.hlay.addWidget(self.labl1)
        self.hlay.addWidget(self.EXP)
        self.hlay.addWidget(self.labl2)
        self.hlay.addWidget(self.MIN)
        self.hlay.addWidget(self.labl3)
        self.hlay.addWidget(self.MAX)
        self.msgBox=QMessageBox()
        self.vlay.addLayout(self.hlay)
        self.vlay.addWidget(self.button)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([], [])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
              # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        self.pltwidget = QWidget()
        self.pltwidget.setLayout(layout)
        self.vlay.addWidget(self.pltwidget)
        container = QWidget()

        container.setLayout(self.vlay)
        # Set the central widget of the Window.
        self.setCentralWidget(container)
        self.setFixedSize(700,500)

# to plot the graphs in the bottom of the page I first of all remove previous plots then take the expression after it was validated and replace every ^ with ** 
# that was to ease the process of rendering the expressions by using the existing python interpreter to evaluate expression on values ranging 
# from min value and max values
    def plot(self,expression,mini,maxi):
        self.pltwidget.deleteLater()
        expression.replace("^","**")
        Y=[]
        X=[i for i in range(mini,maxi+1)]
        for x in range(mini,maxi+1):
            Y.append(eval(expression))
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(X, Y)
        print(X,Y)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
              # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        self.pltwidget = QWidget()
        self.pltwidget.setLayout(layout)
        self.vlay.addWidget(self.pltwidget)
# this function is used as a way to handle certain ways where a user can mess up entering the input 
    def clickHandle(self,checked):
        expinp=False
        min=False
        max=False
        exp=self.EXP.text()        
        if (self.EXP.text() == ""):
            expinp=True
            self.fireAlert("enter an expression")
        elif(self.MIN.text() == ""):
            min=True
            self.fireAlert("enter a minimum value")
        elif(self.MAX.text() == ""):
            max=True
            self.fireAlert("enter a maximum value")
        else:
            exp = exp.lower()
            exp.replace(" ","")
            status,lastright=checkForValidity(exp)
            print (status,lastright)
            if (status=="accepted"):
                minstatus=checkForNumbers(self.MIN.text())
                maxstatus=checkForNumbers(self.MAX.text())
                if not minstatus and not maxstatus:
                    self.fireAlert(f"enter a number for minimum input and maximum input")
                elif not minstatus :
                    self.fireAlert(f"enter a number for minimum input")
                elif not maxstatus :
                    self.fireAlert(f"enter a number for maximum input")
                else:
                    if (int(self.MIN.text()) <= int(self.MAX.text())):
                        self.plot(exp,int(self.MIN.text()),int(self.MAX.text()))
                    else:
                        self.fireAlert("minimum should be smaller then maximum")

            
            else :
                self.fireAlert(f"wrong Expression at <b style=\"color:red;\">{lastright}</b>")
        self.EXP.clear()
        self.MAX.clear()
        self.MIN.clear()


    def fireAlert(self,message):
        self.msgBox = QMessageBox()
        self.msgBox.setText(message)
        self.msgBox.exec()

    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
