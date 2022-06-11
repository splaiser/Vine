import pyodbc
# from PyQt6 import QtWidgets
# from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
# from PyQt6.QtWidgets import QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                             QHBoxLayout, QMessageBox, QPushButton, QTableView)
from PyQt5.QtSql import QSqlTableModel
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from qtable import Ui_MainWindow
import sys, glob, os, os.path
from PyQt5.QtSql import QSqlDatabase


def create_connection(database):
    global final_part
    cur_dir = os.getcwd()
    part_1 = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};FIL={MS Access};"
    part_2 = f"DBQ={cur_dir}\{database}"
    final_part = part_1 + part_2

    db = QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName(final_part)
    if not db.open():
        print("Cannot open database")
        return False
    return True


class TableEditor(QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)

        self.model = QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

        view = QTableView()
        view.setModel(self.model)

        submitButton = QPushButton("Submit")
        submitButton.setDefault(True)
        revertButton = QPushButton("&Revert")
        quitButton = QPushButton("Quit")

        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(submitButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(revertButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        submitButton.clicked.connect(self.submit)
        revertButton.clicked.connect(self.model.revertAll)
        quitButton.clicked.connect(self.close)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Cached Table")

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
            QMessageBox.information(self, "Record", "Jumlah record= %s" % self.model.rowCount())
        else:
            self.model.database().rollback()
            QMessageBox.warning(self, "Cached Table",
                                "The database reported an error: %s" % self.model.lastError().text())


if __name__ == "__main__":
    import sys

    # database = 'E:\Python\Винодельня\*.accdb'  # ":memory:"
    app = QtWidgets.QApplication(sys.argv)
    os.chdir("E:/Python/Винодельня")
    for file in glob.glob("*.accdb"):
        if not create_connection(file):
            sys.exit(app.exec_())

    w = TableEditor(final_part)
    w.show()
    sys.exit(app.exec_())
