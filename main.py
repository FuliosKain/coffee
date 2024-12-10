import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

class CoffeeEspresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Измените на имя вашего интерфейса
        self.connection = sqlite3.connect("coffee.sqlite")
        self.select_data()

    def select_data(self):
        query = "SELECT * FROM coffee"  # Измените на нужный вам запрос
        res = self.connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(5)  # Убедитесь, что количество столбцов соответствует вашей таблице
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeEspresso()
    ex.show()
    sys.exit(app.exec())
