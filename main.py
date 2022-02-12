from tool_box_09_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QTableWidget, QMainWindow
from qt_material import apply_stylesheet
import sys


class Run:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main = QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.main)

        self.set_time = self.window.set_time_timeEdit.time().toString()
        self.set_time = self.window.set_time_timeEdit.timeChanged.connect(self.get_set_time)

        self.window.open_interval_radioButton.clicked.connect(self.open_interval_time)

        # print(self.set_time)
        #
        # self.window.shutdown_timeEdit.timeChanged.connect(self.get_shutdown_time)  # 获取关机时间
        # self.window.create_plan_pushButton.clicked.connect(self.create_shutdown)  # 创建关机计划
        # self.window.cancel_pushButton.clicked.connect(self.cancel_shutdown)  # 取消关机计划
        # self.window.shutdown_now_pushButton.clicked.connect(self.shutdown_now)  # 立即关机
        #
        # self.window.get_wechat_path_pushButton.clicked.connect(self.get_wechat_path)  # 获取微信路径
        # self.window.start_wechat_pushButton.clicked.connect(self.open_wechat)  # 开启微信
        #
        # self.marge_path = os.getcwd()
        # self.window.marge_path_lineEdit.setText(self.marge_path)
        # self.window.custom_path_radioButton.clicked.connect(self.open_get_marge_btu)  # 开启自定义路径按钮
        # self.window.default_path_radioButton.clicked.connect(self.close_get_marge_btu)  # 关闭自定义路径按钮
        # self.window.get_marge_path_pushButton.clicked.connect(self.get_marge_path)  # 获取合并文件夹路径
        # self.window.marge_pushButton.clicked.connect(self.marge_file)  # 合并文件
        #
        # self.window.lock_now_pushButton.clicked.connect(self.lock_window)
        #
        # self.marge_path = self.window.marge_path_lineEdit.text()

        self.apply_stylesheet = apply_stylesheet(self.app, theme='dark_teal.xml')
        self.main.show()
        sys.exit(self.app.exec_())

    def get_set_time(self):
        self.set_time = self.window.set_time_timeEdit.time().toString()
        self.window.textBrowser.append(f'设置时间：{self.set_time}')

    def create_shutdown_plan(self):
        if self.window.set_once_radioButton.isChecked():
            pass

    def open_interval_time(self):
        if self.window.open_interval_radioButton.isChecked():
            self.window.set_interval_time_spinBox.setEnabled(True)
            self.window.label_2.setEnabled(True)
        else:
            self.window.set_interval_time_spinBox.setEnabled(False)
            self.window.label_2.setEnabled(False)

if __name__ == '__main__':
    run = Run()
    run()
