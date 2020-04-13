import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QWidget,QApplication,QAction,qApp,QMainWindow


class Notepad(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.text_area = QTextEdit()

        self.cleanse = QPushButton("Clean")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()

        h_box.addWidget(self.cleanse)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()

        v_box.addWidget(self.text_area)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("The Notepad")
        self.cleanse.clicked.connect(self.text_clean)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)



    def text_clean(self):

        self.text_area.clear()

    def open_file(self):

        file_name = QFileDialog.getOpenFileName(self,"Open File",os.getenv("DESKTOP"))

        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())



    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))

        with open(file_name[0],"w") as file:

            file.write(self.text_area.toPlainText())




class Menu(QMainWindow):
    def __init__(self):
        
        super().__init__()

        self.window = Notepad()

        self.setCentralWidget(self.window)

        self.create_menu()

        self.setWindowTitle("Text Editor")

        self.show()

    def create_menu(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")

        open_file_2 = QAction("Open File",self)
        open_file_2.setShortcut("Ctrl+O")

        save_file_2 = QAction("Save File",self)
        save_file_2.setShortcut("Ctrl+S")

        cleanse_2 = QAction("Clear",self)
        cleanse_2.setShortcut("Ctrl+D")

        cikis_2 = QAction("Quit",self)
        cikis_2.setShortcut("Ctrl+Q")

        file.addAction(open_file_2)
        file.addAction(save_file_2)
        file.addAction(cleanse_2)
        file.addAction(cikis_2)

        file.triggered.connect(self.response)





    def response(self,action):

        if action.text() == "Open File":
            self.window.open_file()

        elif action.text() == "Save file":
            self.window.save_file()

        elif action.text() == "Clear":
            self.window.cleanse()

        elif action.text() == "Quit":
            qApp.quit()











app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())