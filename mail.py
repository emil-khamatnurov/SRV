from Design import *

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BoilerSystem = QtWidgets.QMainWindow()
    ui = Ui_BoilerSystem()
    ui.setupUi(BoilerSystem)
    BoilerSystem.show()

    #Методы обработки кнопок бокового меню
    def M_G():
        ui.Application_pages.setCurrentWidget(ui.observation_)
        ui.Title_of_window.setText("Окно графичекого представления информации")
    def M_S():
        ui.Application_pages.setCurrentWidget(ui.parameter_)
        ui.Title_of_window.setText("Окно параметров")
    def M_Sol():
        ui.Application_pages.setCurrentWidget(ui.Solutions_page)
        ui.Title_of_window.setText("Окно решений")
    ui.Menu_Craph_button.clicked.connect(M_G)
    ui.Menu_stroke_button.clicked.connect(M_S)
    ui.Menu_solutions_button.clicked.connect(M_Sol)

    #блок для часов
    from PyQt5.QtCore import QTime, QTimer
    from PyQt5.QtWidgets import QLCDNumber
    #Класс часов
    class Clock(QLCDNumber):

        def __init__(self, parent=None):
            super(Clock, self).__init__(parent)
            #Создание объекта таймера
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000) #одна секунда
            self.showTime()

        def showTime(self):
            time = QTime.currentTime()
            text = time.toString('hh:mm:ss')
            # if (time.second() % 2) == 0:
            text = text[:2] + ':' + text[3:5] + ':' + text[6:]
            ui.Time_lable.setText(text)



    clock = Clock()
    clock.showTime()
    sys.exit(app.exec_())
