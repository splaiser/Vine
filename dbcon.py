import pyodbc
# from PyQt6 import QtWidgets
# from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
# from PyQt6.QtWidgets import QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                             QHBoxLayout, QMessageBox, QPushButton, QTableView)
from PyQt5.QtSql import QSqlTableModel

from qtable import Ui_MainWindow
import sys


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


if __name__ == '__main__':

    editor = TableEditor('Винодельня_бд')
    editor.show()
    sys.exit(editor.exec_())
