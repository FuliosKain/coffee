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

        # Определите названия столбцов
        column_names = ["ID", "Название", "Тип", "Цена", "Объем", "Калории",
                        "Производитель"]  # Замените на ваши названия

        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(len(column_names))  # Установите количество столбцов
        self.tableWidget.setHorizontalHeaderLabels(column_names)  # Установите заголовки столбцов
        self.tableWidget.setRowCount(0)

        # Установите ширину столбцов 2 и 3
        self.tableWidget.setColumnWidth(1, 200)  # Увеличьте ширину второго столбца (Название)
        self.tableWidget.setColumnWidth(2, 150)  # Увеличьте ширину третьего столбца (Тип)

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
