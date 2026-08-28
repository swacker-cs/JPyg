# when i press the button search for images 
# in the specified folder and apply width height and format to that image
# then save it out and send it to the raspberry via ssh locally
from PySide6.QtWidgets import QApplication, QPushButton , QMainWindow, QLabel, QProgressBar
from PySide6.QtCore import QSize, Qt
import sys
from interface import MainWindow
from imageProcesser import readDir, processImages

def processHandler():
    images = readDir(window.selectedDir)

    try: 
        size = int(window.inputSize.text())
    except ValueError:
        size = 4000
        print("Couldn't convert variable inputSize to int.")

    processImages(images, window.selectedOutDir, size)


#the code that will actually run when the py file is executed:

app= QApplication(sys.argv)

#creating interface instance
window = MainWindow()
window.show()      

#calling the processHandler function
window.processButton.clicked.connect(processHandler)
app.exec()



