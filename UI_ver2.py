# -*- coding: utf-8 -*-
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from runge_kutt_test import *
from runge_tutt_main1_1 import *
from runge_kutt_main1 import *
from runge_kutt_main2 import *


class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    N = 10
    X0 = 1
    U0 = 1
    h = 0.1
    eps = 0.000001

    def set_N(self, N):
        self.N = N
        print(N)

    def set_X0(self, X0):
        self.X0 = X0
        print(X0)

    def set_U0(self, U0):
        self.U0 = U0
        print(U0)

    def set_h(self, h):
        self.h = h
        print(h)

    def set_eps(self, eps):
        self.eps = eps

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self, function_index):
        functions = {
            1: RK_Method_Without_ce(self.N, self.X0, self.U0, self.h),
            2: RK_Method_Without_ce_main_1(self.N, self.X0, self.U0, self.h),
            3: RK_Method_Without_ce_main_2(self.N, self.X0, self.U0, self.h),
            4: RK_Method_halfhope_Without_ce(self.N, self.X0, self.U0, self.h),
            5: RK_Method_halfhope_Without_ce_main_1(self.N, self.X0, self.U0, self.h),
            6: RK_Method_halfhope_Without_ce_main_2(self.N, self.X0, self.U0, self.h),
            7: RK_Method_With_ce(self.N, self.X0, self.U0, self.h, self.eps),
            8: RK_Method_With_ce_main_1(self.N, self.X0, self.U0, self.h, self.eps),
            9: RK_Method_With_ce_main_2(self.N, self.X0, self.U0, self.h, self.eps)
        }

        x = functions[function_index][0]
        y = functions[function_index][1]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        ax.plot(x, y, linestyle='-', color='#008000')
        self.canvas.draw()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph_widget = PlotWidget()
        self.graph_widget.setGeometry(QtCore.QRect(460, 10, 551, 361))
        self.graph_widget.setStyleSheet("background-color: white")
        self.graph_widget.setObjectName("graph_widget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 281, 151))
        self.tabWidget.setObjectName("tabWidget")
        self.test_tab = QtWidgets.QWidget()
        self.test_tab.setObjectName("test_tab")
        self.plt_test = QtWidgets.QPushButton(self.test_tab)
        self.plt_test.setGeometry(QtCore.QRect(10, 60, 131, 51))
        self.plt_test.setObjectName("plt_test")
        self.clear_test = QtWidgets.QPushButton(self.test_tab)
        self.clear_test.setGeometry(QtCore.QRect(160, 60, 101, 51))
        self.clear_test.setObjectName("clear_test")
        self.radioButton_3 = QtWidgets.QRadioButton(self.test_tab)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 30, 161, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.onClicked)


        self.radioButton_4 = QtWidgets.QRadioButton(self.test_tab)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 10, 161, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.toggled.connect(self.onClicked)

        self.tabWidget.addTab(self.test_tab, "")
        self.main1_tab = QtWidgets.QWidget()
        self.main1_tab.setObjectName("main1_tab")
        self.plot_main1 = QtWidgets.QPushButton(self.main1_tab)
        self.plot_main1.setGeometry(QtCore.QRect(160, 60, 101, 51))
        self.plot_main1.setObjectName("plot_main1")
        self.clear_main1 = QtWidgets.QPushButton(self.main1_tab)
        self.clear_main1.setGeometry(QtCore.QRect(10, 60, 131, 51))
        self.clear_main1.setObjectName("clear_main1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.main1_tab)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 10, 161, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.onClicked)

        self.radioButton = QtWidgets.QRadioButton(self.main1_tab)
        self.radioButton.setGeometry(QtCore.QRect(110, 30, 161, 17))
        self.radioButton.setObjectName("radioButton")
        # self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.onClicked)

        self.tabWidget.addTab(self.main1_tab, "")
        self.main2_tab = QtWidgets.QWidget()
        self.main2_tab.setObjectName("main2_tab")
        self.clear_main2 = QtWidgets.QPushButton(self.main2_tab)
        self.clear_main2.setGeometry(QtCore.QRect(160, 60, 101, 51))
        self.clear_main2.setObjectName("clear_main2")
        self.plot_main2 = QtWidgets.QPushButton(self.main2_tab)
        self.plot_main2.setGeometry(QtCore.QRect(10, 60, 131, 51))
        self.plot_main2.setObjectName("plot_main2")

        self.radioButton_5 = QtWidgets.QRadioButton(self.main2_tab)
        self.radioButton_5.setGeometry(QtCore.QRect(110, 30, 161, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.toggled.connect(self.onClicked)


        self.radioButton_6 = QtWidgets.QRadioButton(self.main2_tab)
        self.radioButton_6.setGeometry(QtCore.QRect(110, 10, 161, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.toggled.connect(self.onClicked)

        self.tabWidget.addTab(self.main2_tab, "")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 390, 750, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(PlotWidget.N)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 190, 281, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.steps_PB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.steps_PB.setObjectName("steps_PB")
        self.gridLayout.addWidget(self.steps_PB, 7, 1, 1, 1)
        self.line_exit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_exit.setObjectName("line_exit")
        self.gridLayout.addWidget(self.line_exit, 9, 0, 1, 1)
        self.control_PB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.control_PB.setObjectName("control_PB")
        self.gridLayout.addWidget(self.control_PB, 2, 1, 1, 1)
        self.step_PB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.step_PB.setObjectName("step_PB")
        self.gridLayout.addWidget(self.step_PB, 5, 1, 1, 1)
        self.exit_PB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exit_PB.setObjectName("exit_PB")
        self.gridLayout.addWidget(self.exit_PB, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 2)
        self.line_control_error = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_control_error.setObjectName("line_control_error")
        self.gridLayout.addWidget(self.line_control_error, 2, 0, 1, 1)
        self.line_steps = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_steps.setObjectName("line_steps")
        self.gridLayout.addWidget(self.line_steps, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.line_h = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_h.setObjectName("line_h")
        self.gridLayout.addWidget(self.line_h, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(300, 50, 131, 92))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 2)
        self.control_PB_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.control_PB_2.setObjectName("control_PB_2")
        self.gridLayout_2.addWidget(self.control_PB_2, 1, 1, 1, 1)
        self.line_U0 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.line_U0.setObjectName("line_U0")
        self.gridLayout_2.addWidget(self.line_U0, 3, 0, 1, 1)
        self.line_X0 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.line_X0.setObjectName("line_X0")
        self.gridLayout_2.addWidget(self.line_X0, 1, 0, 1, 1)
        self.U0_PB = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.U0_PB.setObjectName("U0_PB")
        self.gridLayout_2.addWidget(self.U0_PB, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.l = QVBoxLayout(self.centralwidget)
        self.bl = QHBoxLayout(self.centralwidget)

        self.l2 = QVBoxLayout(self.graph_widget)
        self.l.addWidget(self.graph_widget)
        self.l2.addWidget(self.graph_widget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plt_test.setText(_translate("MainWindow", "Plot"))
        self.clear_test.setText(_translate("MainWindow", "Clear"))
        self.radioButton_3.setText(_translate("MainWindow", "Без контроля погрешности"))
        self.radioButton_4.setText(_translate("MainWindow", "С контролем погрешности"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_tab), _translate("MainWindow", "Тестовая"))
        self.plot_main1.setText(_translate("MainWindow", "Clear"))
        self.clear_main1.setText(_translate("MainWindow", "Plot"))
        self.radioButton_2.setText(_translate("MainWindow", "С контролем погрешности"))
        self.radioButton.setText(_translate("MainWindow", "Без контроля погрешности"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main1_tab), _translate("MainWindow", "Основная 1"))
        self.clear_main2.setText(_translate("MainWindow", "Clear"))
        self.plot_main2.setText(_translate("MainWindow", "Plot"))
        self.radioButton_5.setText(_translate("MainWindow", "Без контроля погрешности"))
        self.radioButton_6.setText(_translate("MainWindow", "С контролем погрешности"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main2_tab), _translate("MainWindow", "Основная 2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Xi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "hi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Vi^V^i"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Делений"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Удвоений"))
        self.steps_PB.setText(_translate("MainWindow", "Enter"))
        self.control_PB.setText(_translate("MainWindow", "Enter"))
        self.step_PB.setText(_translate("MainWindow", "Enter"))
        self.exit_PB.setText(_translate("MainWindow", "Enter"))
        self.label_4.setText(_translate("MainWindow", "Точность выхода за границу"))
        self.label_2.setText(_translate("MainWindow", "Число шагов"))
        self.label.setText(_translate("MainWindow", " Контроль погрешности"))
        self.label_3.setText(_translate("MainWindow", "Шаг"))
        self.label_6.setText(_translate("MainWindow", "U0"))
        self.control_PB_2.setText(_translate("MainWindow", "Enter"))
        self.U0_PB.setText(_translate("MainWindow", "Enter"))
        self.label_5.setText(_translate("MainWindow", "X0:"))

        self.step_PB.clicked.connect(lambda: PlotWidget.set_h(PlotWidget, float(self.line_h.text())))
        self.control_PB_2.clicked.connect(lambda: PlotWidget.set_X0(PlotWidget, float(self.line_X0.text())))
        self.U0_PB.clicked.connect(lambda: PlotWidget.set_U0(PlotWidget, float(self.line_U0.text())))
        self.steps_PB.clicked.connect(lambda: PlotWidget.set_N(PlotWidget, int(self.line_steps.text())))
        self.steps_PB.clicked.connect(lambda: self.tableWidget.setRowCount(PlotWidget.N))

    def onClicked(self):
        if self.radioButton.isChecked():
            self.clear_main1.clicked.connect(lambda: (self.graph_widget.plot(2)))
            self.plot_main1.clicked.connect(lambda: self.tableWidget.clear())
            self.clear_main1.clicked.connect(lambda: self.setTable_without_ce(2))
            self.plot_main1.clicked.connect(self.clear)
        if self.radioButton_2.isChecked():
            self.clear_main1.clicked.connect(lambda: (self.graph_widget.plot(8)))
            self.plot_main1.clicked.connect(lambda: self.tableWidget.clear())
            self.clear_main1.clicked.connect(lambda: self.setTable_with_ce(8))
            self.plot_main1.clicked.connect(self.clear)
        if self.radioButton_5.isChecked():
            self.plot_main2.clicked.connect(lambda: (self.graph_widget.plot(3)))
            self.plot_main2.clicked.connect(lambda: self.tableWidget.clear())
            self.plot_main2.clicked.connect(lambda: self.setTable_without_ce(3))
            self.clear_main2.clicked.connect(self.clear)
        if self.radioButton_6.isChecked():
            self.plot_main2.clicked.connect(lambda: (self.graph_widget.plot(9)))
            self.plot_main2.clicked.connect(lambda: self.tableWidget.clear())
            self.plot_main2.clicked.connect(lambda: self.setTable_with_ce(9))
            self.clear_main2.clicked.connect(self.clear)
        if self.radioButton_3.isChecked():
            self.plt_test.clicked.connect(lambda: (self.graph_widget.plot(1)))
            self.plt_test.clicked.connect(lambda: self.tableWidget.clear())
            self.plt_test.clicked.connect(lambda: self.setTable_without_ce(1))
            self.clear_test.clicked.connect(self.clear)
        if self.radioButton_4.isChecked():
            self.plt_test.clicked.connect(lambda: (self.graph_widget.plot(7)))
            self.plt_test.clicked.connect(lambda:self.tableWidget.clear())
            self.plt_test.clicked.connect(lambda: self.setTable_with_ce(7))
            self.clear_test.clicked.connect(self.clear)

    def returnFunc(self, funcindex):
        functions = {
            1: RK_Method_Without_ce(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            2: RK_Method_Without_ce_main_1(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            3: RK_Method_Without_ce_main_2(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            4: RK_Method_halfhope_Without_ce(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            5: RK_Method_halfhope_Without_ce_main_1(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            6: RK_Method_halfhope_Without_ce_main_2(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h),
            7: RK_Method_With_ce(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h, PlotWidget.eps),
            8: RK_Method_With_ce_main_1(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h, PlotWidget.eps),
            9: RK_Method_With_ce_main_2(PlotWidget.N, PlotWidget.X0, PlotWidget.U0, PlotWidget.h, PlotWidget.eps)
        }
        return functions[funcindex]

    def setTable_without_ce(self, funcindex):
        for i in range(PlotWidget.N):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.returnFunc(funcindex)[0][i])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(PlotWidget.h)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.returnFunc(funcindex)[1][i])))

    def setTable_with_ce(self, funcindex):

        for i in range(len(self.returnFunc(funcindex)[0])):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.returnFunc(funcindex)[0][i])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.returnFunc(funcindex)[2][i])))
            #self.tableWidget.setItem(i, 1, QTableWidgetItem(str(PlotWidget.h)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.returnFunc(funcindex)[1][i])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.returnFunc(funcindex)[3][i])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.returnFunc(funcindex)[4][i])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.returnFunc(funcindex)[5][i])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(self.returnFunc(funcindex)[6][i])))
    def clear(self):
        self.graph_widget.figure.clear()
        self.graph_widget.canvas.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
