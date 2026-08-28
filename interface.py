from PySide6.QtWidgets import QApplication , QPushButton , QMainWindow , QWidget, QVBoxLayout, QLineEdit, QLabel, QProgressBar, QHBoxLayout, QFileDialog, QMessageBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from pathlib import Path
import platformdirs
import os
import sys

appDataDir = Path(platformdirs.user_data_dir("JPyg", "StefanRWacker"))
appDataDir.mkdir(parents=True, exist_ok=True)
configInputPath = appDataDir / "inputDirectory.txt"
configOutputPath = appDataDir / "outputDirectory.txt"

if configInputPath.exists():
     inputDirectory = configInputPath.read_text()
else:
     inputDirectory = str(Path(__file__).parent)

if configOutputPath.exists():
     outputDirectory = configOutputPath.read_text()
else:
     outputDirectory = str(Path(__file__).parent)

def shorten_path(selectedDir, length):
        return Path(*Path(selectedDir).parts[-length:])

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    return base_path / relative_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(str(resource_path("app_icon.ico"))))
        self.setStyleSheet("""
        QMainWindow {
        background-color: #050505;
        }
        QPushButton {
        color: #050505;
        background-color: #dfff0f;
        padding: 5px;
        font-size: 16px;
        }
        QLabel {
        color: #ffffff;
        font-size:12px;
        }
        QMenuBar{
        background-color: #120525;
        color: #ffffff;
        padding:4px;
        }
        QMessageBox{
        background-color: #050505;
        }
        """)

        self.selectedDir = inputDirectory
        self.selectedOutDir = outputDirectory
        self.setWindowTitle("JPyg")

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)
        #container.setFixedSize(QSize(400, 600))

        dir_container = QWidget()
        dir_layout = QHBoxLayout(dir_container)

        out_container = QWidget()
        out_layout = QHBoxLayout(out_container)

        size_container = QWidget()
        size_layout = QHBoxLayout(size_container)

        #input Directory selection
        self.dirButton = QPushButton("Select Image Directory")
        self.dirButton.clicked.connect(self.chooseinputDirectory)

        self.dirLabel = QLabel(inputDirectory)

        #output Directory selection
        self.outputLabel = QLabel(outputDirectory) 
        self.outputButton = QPushButton("Select Output Directory")
        self.outputButton.clicked.connect(self.chooseOutputDirectory)
        


        #do the thing button
        self.processButton = QPushButton("Process Images")

        self.sizeLabel = QLabel("Maximum Image Dimension(px):" )
        self.inputSize = QLineEdit("4000")

        dir_layout.addWidget(self.dirLabel)
        dir_layout.addWidget(self.dirButton)

        out_layout.addWidget(self.outputLabel)
        out_layout.addWidget(self.outputButton)

        size_layout.addWidget(self.sizeLabel)
        size_layout.addWidget(self.inputSize)


        layout.addWidget(size_container)
        layout.addWidget(dir_container)
        layout.addWidget(out_container)
        layout.addWidget(size_container)
        layout.addWidget(self.processButton)

        menubar = self.menuBar()

        settingsMenu = menubar.addMenu("Settings")
        settingAction = settingsMenu.addAction("Set Selected Folder as Standard")
        settingAction.triggered.connect(self.writeFolderPresets)
        settingAction2 = settingsMenu.addAction("Reset")
        settingAction2.triggered.connect(self.resetFolderPreset)
        aboutMenu = menubar.addMenu("?")
        aboutAction = aboutMenu.addAction("About")
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About", "Author: Stefan R. Wacker - Connect with me via art.wacker@gmail.com") )


    def chooseinputDirectory(self):
        selectedDir = QFileDialog.getExistingDirectory(self, "Please pick a inputDirectory...", inputDirectory)
        shortenedDir = "..." + os.sep + str(shorten_path(selectedDir, 4))
        if selectedDir:
            self.selectedDir = selectedDir
            self.dirLabel.setText(shortenedDir)

    def chooseOutputDirectory(self):
        selectedOutDir = QFileDialog.getExistingDirectory(self, "Please pick a inputDirectory...", outputDirectory)
        shortenedDir = "..." + os.sep + str(shorten_path(selectedOutDir, 4))
        if selectedOutDir:
            self.selectedOutDir = selectedOutDir
            self.outputLabel.setText(shortenedDir)

    def resetFolderPreset(self):
        defaultDir = str(Path.home() / "Pictures")
        configInputPath.write_text(defaultDir)
        self.dirLabel.setText("..." + os.sep + str(shorten_path(defaultDir, 4)))
        configOutputPath.write_text(defaultDir)
        self.outputLabel.setText("..." + os.sep + str(shorten_path(defaultDir, 4)))

    def writeFolderPresets(self):
        configInputPath.write_text(self.selectedDir)
        configOutputPath.write_text(self.selectedOutDir)

         
