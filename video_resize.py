from PyQt5 import QtWidgets, QtGui
import cv2
import os
import sys

from GUI import Ui_MainWindow
from frame_resize import frame_resize


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Video Resize")
        self.save.clicked.connect(self.file_save)
        self.preview.clicked.connect(self.resized_preview)
        self.open.clicked.connect(self.file_open)
        self.h_size.setText("2762")
        self.v_size.setText("2061")
        self.v_size.setValidator(QtGui.QIntValidator())
        self.h_size.setValidator(QtGui.QIntValidator())
        self.cap = None

    def file_open(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "select a file", "", "MOV (*.mov);; MPEG-4 (*.mp4);; AVI (*.avi);; All (*.mov *.mp4 *.avi *.mkv)")
        self.cap = cv2.VideoCapture(file)
        filepath, filename = os.path.split(file)
        basename, extension = os.path.splitext(filename)
        self.default_name = os.path.join(filepath, basename+"_Resized")
        self.default_name = self.default_name.replace("/", "\\")

    def video_resize(self):
        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        frame_count = int(self.cap.get(7))
        frame_rate = int(self.cap.get(5))
        h = int(self.h_size.text())
        v = int(self.v_size.text())
        method = self.comboBox.currentText()
        self.process_bar = QtWidgets.QProgressBar(self)
        self.process_bar.setMinimum(0)
        self.process_bar.setMaximum(frame_count)
        self.process_bar.show()
        if self.codec == "MPEG (*.mp4)":
            fourcc = cv2.VideoWriter_fourcc(*"mpeg")
        else:
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
        output_file = cv2.VideoWriter(self.save_filename, fourcc, frame_rate, (h, v))
        position = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                new_frame = frame_resize(frame, frame_width, frame_height, h, v, method)
                output_file.write(new_frame)
                position += 1
                self.process_bar_value(position, frame_count)
                QtGui.QGuiApplication.processEvents()
        self.cap.release()
        output_file.release()

    def file_save(self):
        if not self.cap:
            QtWidgets.QMessageBox.information(self, "Information", "Please select a file first.")
        else:
            self.save_filename, self.codec = QtWidgets.QFileDialog.getSaveFileName(self, "save file", self.default_name, "MPEG (*.mp4);;Mov (*.mov)")
            if self.save_filename:
                self.video_resize()

    def resized_preview(self):
        pass

    def process_bar_value(self, value, count):
        self.process_bar.setValue(value)
        if value == count:
            self.process_bar.hide()
            QtWidgets.QMessageBox.information(self, "Information", "Resize finished")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



