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
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.save.clicked.connect(self.file_save)
        self.preview.clicked.connect(self.resized_preview)
        self.open.clicked.connect(self.file_open)
        self.h_size.setText("2762")
        self.v_size.setText("2061")
        self.v_size.setValidator(QtGui.QIntValidator())
        self.h_size.setValidator(QtGui.QIntValidator())
        self.file = None

    def file_open(self):
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "select a file", "", "MOV (*.mov);; MPEG-4 (*.mp4);; AVI (*.avi);; All (*.mov *.mp4 *.avi *.mkv)")
        filepath, filename = os.path.split(self.file)
        basename, extension = os.path.splitext(filename)
        self.default_name = os.path.join(filepath, basename+"_Resized").replace("/", "\\")

    def video_resize(self, isSave = False):
        self.cap = cv2.VideoCapture(self.file)
        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        frame_count = int(self.cap.get(7))
        frame_rate = int(self.cap.get(5))
        h = int(self.h_size.text())
        v = int(self.v_size.text())
        method = self.comboBox.currentText()
        if isSave:
            self.progressBar.setMaximum(frame_count)
            output_file = cv2.VideoWriter(self.save_filename, -1, frame_rate, (h, v))
            position = 0
        else:
            cv2.namedWindow("Preview", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                new_frame = frame_resize(frame, frame_width, frame_height, h, v, method)
                if isSave:
                    output_file.write(new_frame)
                    position += 1
                    self.process_bar_value(position, frame_count)
                    QtGui.QGuiApplication.processEvents()
                    wait_time = 1
                else:
                    cv2.imshow("Preview", new_frame)
                    wait_time = int(1000/frame_rate)
            else:
                break
            key = cv2.waitKey(wait_time)
            if not isSave:
                if key == 27:
                    break
                elif key == 32:
                    cv2.setWindowProperty("Preview", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        self.cap.release()
        if isSave:
            output_file.release()
        else:
            cv2.destroyAllWindows()

    def file_save(self):
        if not self.file:
            QtWidgets.QMessageBox.information(self, "Information", "Please select a file first.")
        else:
            self.save_filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "save file", self.default_name, "MPEG (*.mp4);;Mov (*.mov)")
            if self.save_filename:
                self.video_resize(True)

    def resized_preview(self):
        if self.file:
            self.video_resize(False)

    def process_bar_value(self, value, count):
        self.progressBar.setValue(value)
        if value == count:
            self.progressBar.setValue(0)
            QtWidgets.QMessageBox.information(self, "Information", "Resize finished")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



