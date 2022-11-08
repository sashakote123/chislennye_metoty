import random
import sys
import numpy as np  # Для вычислений
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.Qt import *
from runge_kutt_test import RK_Method_Without_ce
from runge_tutt_main1_1 import RK_Method_Without_ce_main_1
from runge_kutt_main2 import RK_Method_Without_ce_main_2
from PyQt5 import QtCore, QtGui, QtWidgets

# from uitest import Ui_MainWindow

N=100
X0= 1
U0 =1
h = 0.01

def set_params(N):
    return N



class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self, function_index):
        functions = {
            1: RK_Method_Without_ce(N, X0, U0, h),
            2: RK_Method_Without_ce_main_1(N, X0, U0, h),
            3: RK_Method_Without_ce_main_2(N, X0, U0, h)
        }

        # function_index = random.randint(1,3)
        function = functions[function_index]
        print(function_index)
        x = functions[function_index][0]

        y = functions[function_index][1]

        # print(x)
        # print(y)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        ax.plot(x, y, linestyle='-', color='#008000')
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()
        self.connectUi()

    def initUi(self):
        self.centralWidget = QWidget(self)

        self.l = QVBoxLayout(self.centralWidget)
        self.bl = QHBoxLayout(self.centralWidget)

        self.plotWidget = PlotWidget()

        self.plotButton = QPushButton('Plot')
        self.clearButton = QPushButton('Clear')

        self.plotButton.setStyleSheet('font-size: 12pt; font-weight: 530;')
        self.clearButton.setStyleSheet('font-size: 12pt; font-weight: 530;')

        self.bl.addWidget(self.plotButton)
        self.bl.addWidget(self.clearButton)

        self.l.addLayout(self.bl)
        self.l.addWidget(self.plotWidget)

        self.setCentralWidget(self.centralWidget)

    def connectUi(self):
        self.plotButton.clicked.connect(self.plotWidget.plot)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        self.plotWidget.figure.clear()
        self.plotWidget.canvas.draw()


if __name__ == "__main__":
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())
