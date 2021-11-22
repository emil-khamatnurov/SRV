# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/emilhamatnurov/PycharmProjects/SVR/Design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BoilerSystem(object):
    def setupUi(self, BoilerSystem):
        BoilerSystem.setObjectName("BoilerSystem")
        BoilerSystem.resize(792, 601)
        self.centralwidget = QtWidgets.QWidget(BoilerSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.menu = QtWidgets.QFrame(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 50, 51, 531))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(182, 240, 107);")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.Menu_Craph_button = QtWidgets.QPushButton(self.menu)
        self.Menu_Craph_button.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Menu_Craph_button.setFont(font)
        self.Menu_Craph_button.setObjectName("Menu_Craph_button")
        self.Menu_stroke_button = QtWidgets.QPushButton(self.menu)
        self.Menu_stroke_button.setGeometry(QtCore.QRect(0, 50, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Menu_stroke_button.setFont(font)
        self.Menu_stroke_button.setObjectName("Menu_stroke_button")
        self.Menu_solutions_button = QtWidgets.QPushButton(self.menu)
        self.Menu_solutions_button.setGeometry(QtCore.QRect(0, 100, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Menu_solutions_button.setFont(font)
        self.Menu_solutions_button.setObjectName("Menu_solutions_button")
        self.Units_of_Title = QtWidgets.QFrame(self.centralwidget)
        self.Units_of_Title.setGeometry(QtCore.QRect(0, 0, 792, 50))
        self.Units_of_Title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Units_of_Title.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.Units_of_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Units_of_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Units_of_Title.setObjectName("Units_of_Title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Units_of_Title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title_of_window = QtWidgets.QLabel(self.Units_of_Title)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Title_of_window.setFont(font)
        self.Title_of_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title_of_window.setStyleSheet("color: rgb(191, 191, 191);")
        self.Title_of_window.setObjectName("Title_of_window")
        self.horizontalLayout.addWidget(self.Title_of_window)
        self.Units_of_menu = QtWidgets.QFrame(self.centralwidget)
        self.Units_of_menu.setGeometry(QtCore.QRect(50, 50, 742, 531))
        self.Units_of_menu.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.Units_of_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Units_of_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Units_of_menu.setObjectName("Units_of_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Units_of_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Application_pages = QtWidgets.QStackedWidget(self.Units_of_menu)
        self.Application_pages.setStyleSheet("color: rgb(255, 255, 255);")
        self.Application_pages.setObjectName("Application_pages")
        self.observation_ = QtWidgets.QWidget()
        self.observation_.setStyleSheet("background-color: rgb(212, 216, 216);")
        self.observation_.setObjectName("observation_")
        self.Units_group1 = QtWidgets.QGroupBox(self.observation_)
        self.Units_group1.setGeometry(QtCore.QRect(0, 0, 721, 511))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Units_group1.setFont(font)
        self.Units_group1.setStyleSheet("background-color: rgb(184, 255, 115);\n"
"color: rgb(64, 64, 64);")
        self.Units_group1.setObjectName("Units_group1")
        self.gridLayout = QtWidgets.QGridLayout(self.Units_group1)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.Units_group1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)
        self.Graphic = QtWidgets.QGraphicsView(self.Units_group1)
        self.Graphic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Graphic.setObjectName("Graphic")
        self.gridLayout.addWidget(self.Graphic, 0, 0, 2, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.Units_group1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.Units_group1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Gr_boiler_title = QtWidgets.QLabel(self.Units_group1)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        self.Gr_boiler_title.setFont(font)
        self.Gr_boiler_title.setObjectName("Gr_boiler_title")
        self.verticalLayout_2.addWidget(self.Gr_boiler_title)
        self.boiler_capacity = QtWidgets.QGraphicsView(self.Units_group1)
        self.boiler_capacity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.boiler_capacity.setObjectName("boiler_capacity")
        self.verticalLayout_2.addWidget(self.boiler_capacity)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.Application_pages.addWidget(self.observation_)
        self.parameter_ = QtWidgets.QWidget()
        self.parameter_.setMinimumSize(QtCore.QSize(716, 505))
        self.parameter_.setStyleSheet("background-color: rgb(183, 232, 103);\n"
"color: rgb(64, 64, 64);")
        self.parameter_.setObjectName("parameter_")
        self.Units_group2 = QtWidgets.QGroupBox(self.parameter_)
        self.Units_group2.setGeometry(QtCore.QRect(0, 0, 721, 511))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Units_group2.setFont(font)
        self.Units_group2.setStyleSheet("background-color: rgb(184, 255, 115);")
        self.Units_group2.setObjectName("Units_group2")
        self.Values_table = QtWidgets.QTableWidget(self.Units_group2)
        self.Values_table.setGeometry(QtCore.QRect(7, 30, 701, 331))
        self.Values_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Values_table.setObjectName("Values_table")
        self.Values_table.setColumnCount(0)
        self.Values_table.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(self.Units_group2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 370, 691, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Lables_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Lables_layout.setContentsMargins(3, 3, 3, 3)
        self.Lables_layout.setObjectName("Lables_layout")
        self.Boiling_time = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Boiling_time.setFont(font)
        self.Boiling_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Boiling_time.setObjectName("Boiling_time")
        self.Lables_layout.addWidget(self.Boiling_time, 1, 0, 1, 1)
        self.t_boiler = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.t_boiler.setFont(font)
        self.t_boiler.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t_boiler.setObjectName("t_boiler")
        self.Lables_layout.addWidget(self.t_boiler, 0, 0, 1, 1)
        self.Electricity_consumption = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Electricity_consumption.setFont(font)
        self.Electricity_consumption.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Electricity_consumption.setObjectName("Electricity_consumption")
        self.Lables_layout.addWidget(self.Electricity_consumption, 0, 1, 1, 1)
        self.Power_lable = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Power_lable.setFont(font)
        self.Power_lable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Power_lable.setObjectName("Power_lable")
        self.Lables_layout.addWidget(self.Power_lable, 1, 1, 1, 1)
        self.Application_pages.addWidget(self.parameter_)
        self.Solutions_page = QtWidgets.QWidget()
        self.Solutions_page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Solutions_page.setObjectName("Solutions_page")
        self.Units_group3 = QtWidgets.QGroupBox(self.Solutions_page)
        self.Units_group3.setGeometry(QtCore.QRect(0, 0, 721, 511))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Units_group3.setFont(font)
        self.Units_group3.setStyleSheet("background-color: rgb(184, 255, 115);\n"
"\n"
"color: rgb(49, 49, 49);")
        self.Units_group3.setObjectName("Units_group3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Units_group3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 29, 251, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.practice_ = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.practice_.setContentsMargins(0, 0, 0, 0)
        self.practice_.setObjectName("practice_")
        self.Reload_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Reload_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Reload_button.setObjectName("Reload_button")
        self.practice_.addWidget(self.Reload_button)
        self.Call_service = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Call_service.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Call_service.setObjectName("Call_service")
        self.practice_.addWidget(self.Call_service)
        self.Enter_electricity_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Enter_electricity_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Enter_electricity_button.setObjectName("Enter_electricity_button")
        self.practice_.addWidget(self.Enter_electricity_button)
        self.Error_window = QtWidgets.QTextBrowser(self.Units_group3)
        self.Error_window.setGeometry(QtCore.QRect(270, 30, 431, 461))
        self.Error_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Error_window.setObjectName("Error_window")
        self.Application_pages.addWidget(self.Solutions_page)
        self.verticalLayout.addWidget(self.Application_pages)
        self.Status_bar = QtWidgets.QFrame(self.centralwidget)
        self.Status_bar.setGeometry(QtCore.QRect(0, 579, 792, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.Status_bar.setFont(font)
        self.Status_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status_bar.setObjectName("Status_bar")
        self.lab_tm_title = QtWidgets.QLabel(self.Status_bar)
        self.lab_tm_title.setGeometry(QtCore.QRect(50, 3, 51, 16))
        self.lab_tm_title.setObjectName("lab_tm_title")
        self.Time_lable = QtWidgets.QLabel(self.Status_bar)
        self.Time_lable.setGeometry(QtCore.QRect(100, 4, 81, 16))
        self.Time_lable.setObjectName("Time_lable")
        self.Notification_line = QtWidgets.QLabel(self.Status_bar)
        self.Notification_line.setGeometry(QtCore.QRect(335, 4, 451, 16))
        self.Notification_line.setObjectName("Notification_line")
        BoilerSystem.setCentralWidget(self.centralwidget)

        self.retranslateUi(BoilerSystem)
        self.Application_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BoilerSystem)

    def retranslateUi(self, BoilerSystem):
        _translate = QtCore.QCoreApplication.translate
        BoilerSystem.setWindowTitle(_translate("BoilerSystem", "Система бойлера"))
        self.Menu_Craph_button.setText(_translate("BoilerSystem", "GRAPH"))
        self.Menu_stroke_button.setText(_translate("BoilerSystem", "STR"))
        self.Menu_solutions_button.setText(_translate("BoilerSystem", "SOL"))
        self.Title_of_window.setText(_translate("BoilerSystem", "Окно графичекого представления информации"))
        self.Units_group1.setTitle(_translate("BoilerSystem", "Графическое отображение"))
        self.pushButton_2.setText(_translate("BoilerSystem", "Заполнить бойлер"))
        self.pushButton.setText(_translate("BoilerSystem", "Включить нагрев"))
        self.Gr_boiler_title.setText(_translate("BoilerSystem", "Состояние бойлера"))
        self.Units_group2.setTitle(_translate("BoilerSystem", "Параметры и таблица"))
        self.Boiling_time.setText(_translate("BoilerSystem", "Время нагрева:"))
        self.t_boiler.setText(_translate("BoilerSystem", "Температура бойлера:"))
        self.Electricity_consumption.setText(_translate("BoilerSystem", "Расходы на электричество:"))
        self.Power_lable.setText(_translate("BoilerSystem", "Мощность нагрева:"))
        self.Units_group3.setTitle(_translate("BoilerSystem", "Отработка исключений"))
        self.Reload_button.setText(_translate("BoilerSystem", "Перезагрузить устройство"))
        self.Call_service.setText(_translate("BoilerSystem", "Вызвать сервис"))
        self.Enter_electricity_button.setText(_translate("BoilerSystem", "Подключить электричество"))
        self.lab_tm_title.setText(_translate("BoilerSystem", "Время:"))
        self.Time_lable.setText(_translate("BoilerSystem", "ХХ.ХХ.ХХХХ"))
        self.Notification_line.setText(_translate("BoilerSystem", "Уведомление:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoilerSystem = QtWidgets.QMainWindow()
    ui = Ui_BoilerSystem()
    ui.setupUi(BoilerSystem)
    BoilerSystem.show()
    sys.exit(app.exec_())