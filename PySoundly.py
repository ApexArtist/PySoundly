import os
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia
import sys

class SoundBrowser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenSoundly - Free Sound Browser")
        self.setGeometry(200, 200, 800, 600)
        self.layout = QtWidgets.QVBoxLayout()

        self.folderButton = QtWidgets.QPushButton("Select Sound Folder")
        self.folderButton.clicked.connect(self.load_folder)
        self.layout.addWidget(self.folderButton)

        self.soundList = QtWidgets.QListWidget()
        self.soundList.itemClicked.connect(self.play_sound)
        self.layout.addWidget(self.soundList)

        self.player = QtMultimedia.QMediaPlayer()

        controlLayout = QtWidgets.QHBoxLayout()
        self.playButton = QtWidgets.QPushButton("▶ Play")
        self.stopButton = QtWidgets.QPushButton("■ Stop")
        self.playButton.clicked.connect(self.resume_sound)
        self.stopButton.clicked.connect(self.stop_sound)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.stopButton)
        self.layout.addLayout(controlLayout)

        self.setLayout(self.layout)

    def load_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.soundList.clear()
            for file in os.listdir(folder):
                if file.lower().endswith((".wav", ".mp3", ".ogg", ".flac")):
                    item = QtWidgets.QListWidgetItem(file)
                    item.setData(QtCore.Qt.UserRole, os.path.join(folder, file))
                    self.soundList.addItem(item)

    def play_sound(self, item):
        filepath = item.data(QtCore.Qt.UserRole)
        url = QtCore.QUrl.fromLocalFile(filepath)
        content = QtMultimedia.QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def resume_sound(self):
        self.player.play()

    def stop_sound(self):
        self.player.stop()

app = QtWidgets.QApplication(sys.argv)
window = SoundBrowser()
window.show()
sys.exit(app.exec_())
