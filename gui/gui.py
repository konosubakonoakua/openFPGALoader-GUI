from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QFileDialog, QMessageBox,
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QPlainTextEdit,
    QMenuBar, QStatusBar,
    QApplication, QMainWindow,
)
from PyQt5.QtCore import QProcess
from data import BOARDS, FPGAS, CABLES

FILE_SUPPORTED = ";;".join([
    '*.mcs',
    '*.bin',
    '*.bit',
    '*.fs',
])


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.board = BOARDS[0]
        self.fpga = 'xc7k325tffg900'
        self.cable = 'digilent_hs2'
        self.fname = None
        self.p = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowTitle("openFPGALoader GUI (only Xilinx for now)")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_layout = QVBoxLayout(self.centralwidget)

        self.cable_layout = QHBoxLayout()
        self.lable_cable = QLabel("Select Cable:")
        self.dropdownlist_cable = QComboBox()
        self.cable_layout.addWidget(self.lable_cable)
        self.cable_layout.addWidget(self.dropdownlist_cable)
        self.main_layout.addLayout(self.cable_layout)

        self.detect_layout = QHBoxLayout()
        self.lable_detect = QLabel("Detect FPGA:")
        self.pushButton_detect = QPushButton("Detect")
        self.detect_layout.addWidget(self.lable_detect)
        self.detect_layout.addWidget(self.pushButton_detect)
        self.main_layout.addLayout(self.detect_layout)

        self.fpga_layout = QHBoxLayout()
        self.lable_fpga = QLabel("Select FPGA:")
        self.dropdownlist_fpga = QComboBox()
        self.fpga_layout.addWidget(self.lable_fpga)
        self.fpga_layout.addWidget(self.dropdownlist_fpga)
        self.main_layout.addLayout(self.fpga_layout)

        self.button_layout = QHBoxLayout()
        self.pushButton_open_file = QPushButton("Open Binary File")
        self.pushButton_download = QPushButton("Download")
        self.pushButton_download.setDisabled(True)
        self.button_layout.addWidget(self.pushButton_open_file)
        self.button_layout.addWidget(self.pushButton_download)
        self.main_layout.addLayout(self.button_layout)

        self.text_console = QPlainTextEdit()
        self.text_console.setReadOnly(True)
        self.main_layout.addWidget(self.text_console)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        for i in FPGAS:
            self.dropdownlist_fpga.addItem(i)

        for i in CABLES:
            self.dropdownlist_cable.addItem(i)

        self.dropdownlist_fpga.setCurrentText('xc7k325tffg900')
        self.dropdownlist_cable.setCurrentText('digilent_hs2')

        self.pushButton_detect.pressed.connect(self.connection)
        self.dropdownlist_cable.activated.connect(self.activated)
        self.pushButton_open_file.pressed.connect(self.openfile)
        self.pushButton_download.pressed.connect(self.start_process)

    def connection(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start(f"pkexec openFPGALoader -c {self.cable} --detect")

    def activated(self):
        # self.board = self.dropdownlist_board.currentText()
        self.fpga = self.dropdownlist_fpga.currentText()
        self.cable = self.dropdownlist_cable.currentText()

    def openfile(self):
        self.fname = QFileDialog.getOpenFileName(None, 'Open file', './', FILE_SUPPORTED)
        self.pushButton_download.setEnabled(True)

    def message(self, s):
        self.text_console.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            cmd = f"pkexec openFPGALoader -c {self.cable} --fpga-part {self.fpga} -f {self.fname[0]} --verbose-level {2}"
            print(cmd)
            self.p.start(cmd)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        #self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    w = QMainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
