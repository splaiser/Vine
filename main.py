from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.Qt import *
import os, os.path, glob, pyodbc
from PyQt5.QtWidgets import QLineEdit, QTableWidgetItem, QAbstractItemView, QTableWidget, QSizeGrip
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush
from PyQt5.QtCore import Qt, QSortFilterProxyModel



    # Функция для получения пути к файлу с БД
def get_path():
    for file in glob.glob("*.accdb"):
        path = f"{os.getcwd()}\{file}"
        return path

    # Класс определяющий визуальную составляющую программы
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Основной экран
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(780)
        MainWindow.setFixedWidth(1480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 1261, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Кнопка номер 3
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;\n"
            "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        # Кнопка номер 2
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # Кнопка номер 1
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        # Кнопка номер 4
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        # Кнопка номер 5
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        # Таблица
        self.tableWidget = QtWidgets.QTableView(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 1430, 581))
        self.tableWidget.setMinimumSize(QtCore.QSize(1330, 551))
        self.tableWidget.setMaximumSize(QtCore.QSize(1430, 581))
        self.tableWidget.setObjectName("tableWidget")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Поле для поиска
        self.search=QtWidgets.QLineEdit(self)
        self.search.setGeometry(40,10,200,35)
        self.search.setPlaceholderText('Поиск по названию')
        self.search.textChanged.connect(self.searching)
        # Поле для поиска
        self.search=QtWidgets.QLineEdit(self)
        self.search.setGeometry(280,10,200,35)
        self.search.setPlaceholderText('Поиск по синониму')
        self.search.textChanged.connect(self.searching2)
        # Поле для поиска
        self.search=QtWidgets.QLineEdit(self)
        self.search.setGeometry(520,10,200,35)
        self.search.setPlaceholderText('Поиск по номеру образца')
        self.search.textChanged.connect(self.searching3)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вино"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить запись"))
        self.pushButton_4.setText(_translate("MainWindow", "Места происхождения"))
        self.pushButton_5.setText(_translate("MainWindow", "Таксономия"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Окно для добавления записи
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Добавление записи')

        self.line_edit_name = QLineEdit()
        self.line_edit_alt_name = QLineEdit()
        self.line_edit_number = QLineEdit()
        self.line_edit_texon = QLineEdit()
        self.line_edit_place = QLineEdit()
        self.line_edit_bio = QLineEdit()
        self.line_edit_pedigree_eng = QLineEdit()
        self.line_edit_pedigree_rus = QLineEdit()
        self.line_edit_geolocation = QLineEdit()
        self.line_edit_storage = QLineEdit()
        self.line_edit_gen_passport = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow('Наименование образца по русски:', self.line_edit_name)
        form_layout.addRow('Синонимы:', self.line_edit_alt_name)
        form_layout.addRow('Номер_образца:', self.line_edit_number)
        form_layout.addRow('Таксономия:', self.line_edit_texon)
        form_layout.addRow('Место происхождения:', self.line_edit_place)
        form_layout.addRow('Биологический статус образца:', self.line_edit_bio)
        form_layout.addRow('Родословная по английски:', self.line_edit_pedigree_eng)
        form_layout.addRow('Родословная по-русски:', self.line_edit_pedigree_rus)
        form_layout.addRow('Местонахождения страховых дублетов:', self.line_edit_geolocation)
        form_layout.addRow('Типы хранения:', self.line_edit_storage)
        form_layout.addRow('Генетический паспорт сорта:', self.line_edit_gen_passport)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

    # Окно для удаление записи
class Dialog2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Удаление записи')
        self.line_edit_number = QLineEdit()
        form_layout = QFormLayout()
        form_layout.addRow('Номер образца для удаления:', self.line_edit_number)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

    # Окно для подсчёта по "Месту происхождения"
class Dialog3(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Места происхождения')
        self.table_dialog = QtWidgets.QTableView(self)
        self.table_dialog.setFixedSize(480,640)
        self.table_dialog.setObjectName("dialogtableWidget")
        self.model_dialog = QStandardItemModel(self)
        cnxn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                              f"DBQ={get_path()}")
        cursor = cnxn.cursor()
        dt = cursor.execute(
            """
            SELECT "Место происхождения",COUNT("Место происхождения")
            FROM Паспорт
            GROUP BY "Место происхождения"
             """).fetchall()

        for i in range(len(dt)):
            for j in range(2):
                self.model_dialog.setItem(i, j, QStandardItem(str(dt[i][j])))
        self.table_dialog.setModel(self.model_dialog)
        cnxn.close()
    # Окно для подсчёта по "Таксономии"
class Dialog4(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Таксономия')
        self.table_dialog = QtWidgets.QTableView(self)
        self.table_dialog.setFixedSize(480,640)
        self.table_dialog.setObjectName("dialogtableWidget")
        self.model_dialog = QStandardItemModel(self)
        cnxn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                              f"DBQ={get_path()}")
        cursor = cnxn.cursor()
        dt = cursor.execute(
            """
            SELECT "Таксономия                            каталог",COUNT("Таксономия                            каталог")
            FROM Паспорт
            GROUP BY "Таксономия                            каталог"
             """).fetchall()

        for i in range(len(dt)):
            for j in range(2):
                self.model_dialog.setItem(i, j, QStandardItem(str(dt[i][j])))
        self.table_dialog.setModel(self.model_dialog)
        cnxn.close()

    # Основной класс программы
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Подключаем визуальную составляющую
        self.setupUi(self)
        # Подключаем Кнопки
        self.pushButton.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.add_row)
        self.pushButton_2.clicked.connect(self.remove_row)
        self.pushButton_4.clicked.connect(self.place)
        self.pushButton_5.clicked.connect(self.taxo)
        # Подключаем Базу данных
        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setDatabaseName(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={get_path()}")
        self.db.open()
        self.model = QSqlTableModel(self)
        self.model.setTable("Паспорт")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Наименование образца по русски")
        self.model.setHeaderData(1, Qt.Horizontal, "Синонимы")
        self.model.setHeaderData(2, Qt.Horizontal, "Номер_образца")
        self.model.setHeaderData(3, Qt.Horizontal, "Таксономия")
        self.model.setHeaderData(4, Qt.Horizontal, "Место происхождения")
        self.model.setHeaderData(5, Qt.Horizontal, "Биологический статус образца")
        self.model.setHeaderData(6, Qt.Horizontal, "Родословная по английски")
        self.model.setHeaderData(7, Qt.Horizontal, "Родословная по-русски")
        self.model.setHeaderData(8, Qt.Horizontal, "Местонахождения страховых дублетов")
        self.model.setHeaderData(9, Qt.Horizontal, "Типы хранения")
        self.model.setHeaderData(10, Qt.Horizontal, "Генетический паспорт сорта")
        self.model.select()
        self.tableWidget.setModel(self.model)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode
        self.proxy=QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.tableWidget.setModel(self.proxy)

        # Метод класса для поиска по первому столбцу
    def searching(self, text):
        self.proxy.setFilterKeyColumn(0)
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(search)
        # Метод класса для поиска по второму столбцу
    def searching2(self, text):
        self.proxy.setFilterKeyColumn(1)
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(search)
        # Метод класса для поиска по третьему столбцу
    def searching3(self, text):
        self.proxy.setFilterKeyColumn(2)
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(search)
        # Метод класса для добавлении строки
    def add_row(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Внимание', 'Вы отменили добавление записи.')
            return
        name = inputDialog.line_edit_name.text()
        alt_name = inputDialog.line_edit_alt_name.text()
        number = inputDialog.line_edit_number.text()
        texon = inputDialog.line_edit_texon.text()
        place = inputDialog.line_edit_place.text()
        bio = inputDialog.line_edit_bio.text()
        pedigree_eng = inputDialog.line_edit_pedigree_eng.text()
        pedigree_rus = inputDialog.line_edit_pedigree_rus.text()
        geolocation = inputDialog.line_edit_geolocation.text()
        storage = inputDialog.line_edit_storage.text()
        gen_passport = inputDialog.line_edit_gen_passport.text()

        if not number:
            msg = QMessageBox.information(self, 'Внимание', 'Пожалуйста, заполните все поле номера.')
            return

        r = self.model.record()
        r.setValue("Наименование образца по русски", name)
        r.setValue("Синонимы", alt_name)
        r.setValue("Номер_образца", number)
        r.setValue("Таксономия", texon)
        r.setValue("Место происхождения", place)
        r.setValue("Биологический статус образца", bio)
        r.setValue("Родословная по английски", pedigree_eng)
        r.setValue("Родословная по-русски", pedigree_rus)
        r.setValue("Местонахождения", geolocation)
        r.setValue("Типы хранения", storage)
        r.setValue("Генетический паспорт сорта", gen_passport)
        self.model.insertRecord(-1, r)
        self.model.select()
        # Метод класса для удаления строки
    def remove_row(self):
        row = self.tableWidget.currentIndex().row()
        if row == -1:
            msg = QMessageBox.information(self, 'Внимание', 'Выберите запись для удаления.')
            return

        name = self.model.record(row).value(0)
        alt_name = self.model.record(row).value(1)
        number = self.model.record(row).value(2)
        texon = self.model.record(row).value(3)
        place = self.model.record(row).value(4)
        bio = self.model.record(row).value(5)
        pedigree_eng = self.model.record(row).value(6)
        pedigree_rus = self.model.record(row).value(7)
        geolocation = self.model.record(row).value(8)
        storage = self.model.record(row).value(9)
        gen_passport = self.model.record(row).value(10)

        inputDialog = Dialog()
        inputDialog.setWindowTitle('Удалить запись ???')
        inputDialog.line_edit_name.setText(name)
        inputDialog.line_edit_alt_name.setText(alt_name)
        inputDialog.line_edit_number.setText(number)
        inputDialog.line_edit_texon.setText(texon)
        inputDialog.line_edit_place.setText(place)
        inputDialog.line_edit_bio.setText(bio)
        inputDialog.line_edit_pedigree_eng.setText(pedigree_eng)
        inputDialog.line_edit_pedigree_rus.setText(pedigree_rus)
        inputDialog.line_edit_geolocation.setText(geolocation)
        inputDialog.line_edit_storage.setText(storage)
        inputDialog.line_edit_gen_passport.setText(gen_passport)

        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
            return

        self.model.removeRow(self.tableWidget.currentIndex().row())  # Удалить запись   !!!
        self.model.select()  # Удалить запись   !!!

        msg = QMessageBox.information(self, 'Успех', 'Запись удалена.')
        # Метод класса для для подсчёта по "Месту происхождения"
    def place(self):
        tb_dialog = Dialog3()
        rez = tb_dialog.exec()
        # Метод класса для подсчёта по "Таксономии"
    def taxo(self):
        tb_dialog = Dialog4()
        rez = tb_dialog.exec()

    # Запуск программы
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

