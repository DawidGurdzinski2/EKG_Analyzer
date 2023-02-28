from  Algorithms import *
from Mwindow import *
import sys
if __name__ == "__main__":
    #al=Algorithms()
    #al.loadFileCsv('/home/dawid/Desktop/Temat1/pandas-csv/subject-10-sitting.csv')
   # al.loadFilePkl('/home/dawid/Desktop/Temat1/pandas-csv/subject-10-sitting.pkl')
    #al.loadFileWfbd('/home/dawid/Desktop/Temat1/mit-bih-long-term-ecg-database-1.0.0/14046')
   
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

