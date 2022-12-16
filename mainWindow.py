import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

    # Q1: 
    # il ne faut pas oublier de rentrer dans le dossier que notre code python se réside.
    # on voit au print mainwindow.py et execution du programme. si on ecrit d'autre chose
    # à côté de mainwindow.py dans le console, on peut le voir aussi au print
    # Q2.1: ?
    # Q2.2: il faut ajouter de QApplication
    # Q4: on connect les actions aux slots avec "triggered.connect"
    # Q5: en créént une fonction editor
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200,300)
        openAct = QAction(QIcon("open.png"),'&Open...', self)
        openAct.setShortcut("Ctrl+O")
        openAct.setStatusTip('Open file')
        openAct.setToolTip('Open file')
        openAct.triggered.connect(self.openFile)
        
        saveAct = QAction(QIcon("save.png"),'&Save...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save file')
        saveAct.setToolTip('Save file')
        saveAct.triggered.connect(self.saveFile)
        
        copyAct = QAction(QIcon("copy.png"),'&Copy...', self)
        copyAct.setShortcut('Ctrl+C')
        copyAct.setStatusTip('Copy file')
        copyAct.setToolTip('Copy file')
        
        quitAct = QAction(QIcon("quit.png"),'&Quit...', self)
        quitAct.setShortcut('Ctrl+Q')
        quitAct.setStatusTip('Exit file')
        quitAct.setToolTip('Exit file')
        quitAct.triggered.connect(self.quitApp)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(copyAct)
        fileMenu.addAction(quitAct)
        
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(openAct)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAct)
        self.toolbar = self.addToolBar('Copy')
        self.toolbar.addAction(copyAct)
        self.toolbar = self.addToolBar('Quit')
        self.toolbar.addAction(quitAct)

        self.editor()
        
    def openFile(self):
        print("openFile")
        fileName = QFileDialog.getOpenFileName(self, "Open File", "","(*.txt);;( *.html)")
        print(fileName[0])
        self.editor()
        file = QFile(fileName[0])
        file.open(QFile.ReadOnly | QFile.Text)
        f_text = QTextStream(file).readAll()
        self.textEdit.setHtml(f_text)
    def saveFile(self):
        print("saveFile")
        fileName = QFileDialog.getSaveFileName(self, "Save File", "", "(*.txt);;( *.html)")
        print(fileName[0])
        file = open(fileName[0],'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
    def quitApp(self):
        print("quitApp")
        msg = QMessageBox()
        msg.setWindowTitle("Quit App")
        msg.setText("Do you want to leave the app?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec()
        if answer == QMessageBox.Yes:
            QCoreApplication.quit()
        else:
            self.close    

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        
    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("Quit App")
        msg.setText("Do you want to leave the app?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec()
        if answer == QMessageBox.Yes:
           event.accept()
        else:  
            event.ignore()


def main(args):
    print(args)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec() 

if __name__ == "__main__":
    args = sys.argv
    main(args)
    print("execution du programme")

    
    
    
    