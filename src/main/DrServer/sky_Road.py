import threading
import time
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QDateTime, QTimer


class Ui_SkyRoad(object):
    drone_log = []
    dr_dusi = []
    dr_n = []
    log_view_clear_signal = pyqtSignal()

    def __init__(self, SkyRoad):
        self.drone_server = None
        self.centralwidget = QtWidgets.QWidget()
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.lbl_drone_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_log_view = QtWidgets.QLabel(self.centralwidget)
        self.qtext_log_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.qtext_log_view.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.lbl_organization = QtWidgets.QLabel(self.centralwidget)
        self.lbl_user_id = QtWidgets.QLabel(self.centralwidget)
        self.lbl_drone_id = QtWidgets.QLabel(self.centralwidget)
        self.list_ip_addr = QtWidgets.QListWidget(self.centralwidget)
        self.list_drone_id = QtWidgets.QListWidget(self.centralwidget)
        self.list_user_id = QtWidgets.QListWidget(self.centralwidget)
        self.lbl_ip_addr = QtWidgets.QLabel(self.centralwidget)
        self.list_drone = QtWidgets.QListWidget(self.centralwidget)
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_log_view)
        self.timer.start(600000)
        self.setupUi(SkyRoad)

    def setupUi(self, SkyRoad):
        SkyRoad.setObjectName("SkyRoad")
        SkyRoad.resize(1500, 700)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        SkyRoad.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./download.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        SkyRoad.setWindowIcon(icon)
        SkyRoad.setWindowOpacity(1.0)
        SkyRoad.setIconSize(QtCore.QSize(24, 24))
        self.set_status_bar(SkyRoad)
        update_scrollbar = threading.Thread(target=self.set_scrollbar)
        update_scrollbar.daemon = True
        update_scrollbar.start()
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_drone.setObjectName("list_drone")
        self.list_drone.setStyleSheet("border: 1px solid;\n"
                                      "border-left: hidden;\n"
                                      "border-top: hidden;\n"
                                      "border-bottom: hidden;"
                                      )
        self.gridLayout_2.addWidget(self.list_drone, 2, 0, 1, 1)
        self.list_user_id.setObjectName("list_user_id")
        self.list_user_id.setStyleSheet("border: 1px solid;\n"
                                        "border-left: hidden;\n"
                                        "border-top: hidden;\n"
                                        "border-bottom: hidden;"
                                        )
        self.gridLayout_2.addWidget(self.list_user_id, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.list_ip_addr.setObjectName("list_ip_addr")
        self.list_ip_addr.setStyleSheet("border: 1px solid;\n"
                                        "border-left: hidden;\n"
                                        "border-top: hidden;\n"
                                        "border-bottom: hidden;"
                                        )
        self.gridLayout_2.addWidget(self.list_ip_addr, 2, 3, 1, 1)
        self.qtext_log_view.setObjectName("qtext_log_view")
        self.gridLayout_2.addWidget(self.qtext_log_view, 4, 0, 1, 5)
        self.lbl_user_id = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_user_id.setFont(font)
        self.lbl_user_id.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(4, 124, 203);\n"
                                       "border-right: 1px solid;\n"
                                       "border-bottom: 1px solid;\n"
                                       )
        self.lbl_user_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_user_id.setObjectName("lbl_user_id")
        self.gridLayout_2.addWidget(self.lbl_user_id, 1, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_organization.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_organization.setFont(font)
        self.lbl_organization.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(4, 124, 203);\n"
                                            "border-right: 1px solid;\n"
                                            "border-bottom: 1px solid;\n"
                                            "border-left: 1px solid;\n"
                                            )
        self.lbl_organization.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_organization.setObjectName("lbl_organization")
        self.gridLayout_2.addWidget(self.lbl_organization, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_log_view.setFont(font)
        self.lbl_log_view.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(14, 49, 104);\n"
                                        "border: 1px solid;")
        self.lbl_log_view.setObjectName("lbl_log_view")
        self.gridLayout_2.addWidget(self.lbl_log_view, 3, 0, 1, 5)
        self.list_drone_id.setObjectName("list_drone_id")
        self.list_drone_id.setStyleSheet("border: 1px solid;\n"
                                         "border-left: hidden;\n"
                                         "border-top: hidden;\n"
                                         "border-bottom: hidden;"
                                         )
        self.gridLayout_2.addWidget(self.list_drone_id, 2, 2, 1, 1)
        self.lbl_drone_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_drone_info.setFont(font)
        self.lbl_drone_info.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(14, 49, 104);\n"
                                          "border: 1px solid;")
        self.lbl_drone_info.setObjectName("lbl_drone_info")
        self.gridLayout_2.addWidget(self.lbl_drone_info, 0, 0, 1, 4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ip_addr.setFont(font)
        self.lbl_ip_addr.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(4, 124, 203);\n"
                                       "border-right: 1px solid;\n"
                                       "border-bottom: 1px solid;\n"
                                       )
        self.lbl_ip_addr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_ip_addr.setObjectName("lbl_ip_addr")
        self.gridLayout_2.addWidget(self.lbl_ip_addr, 1, 3, 1, 1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_drone_id.setFont(font)
        self.lbl_drone_id.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(4, 124, 203);\n"
                                        "border-right: 1px solid;\n"
                                        "border-bottom: 1px solid;\n"
                                        )
        self.lbl_drone_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_drone_id.setObjectName("lbl_drone_id")
        self.gridLayout_2.addWidget(self.lbl_drone_id, 1, 2, 1, 1)
        self.lbl_log_view.raise_()
        self.qtext_log_view.raise_()
        self.lbl_drone_info.raise_()
        self.list_drone.raise_()
        self.lbl_organization.raise_()
        self.list_user_id.raise_()
        self.list_drone_id.raise_()
        self.list_ip_addr.raise_()
        self.lbl_user_id.raise_()
        self.lbl_ip_addr.raise_()
        self.lbl_drone_id.raise_()
        SkyRoad.setCentralWidget(self.centralwidget)

        self.retranslateUi(SkyRoad)
        QtCore.QMetaObject.connectSlotsByName(SkyRoad)

    def retranslateUi(self, SkyRoad):
        _translate = QtCore.QCoreApplication.translate
        SkyRoad.setWindowTitle(_translate("SkyRoad", "Sky Road"))
        self.lbl_user_id.setText(_translate("SkyRoad", "사용자 정보"))
        self.lbl_organization.setText(_translate("SkyRoad", "회사명"))
        self.lbl_log_view.setText(_translate("SkyRoad",
                                             "<html><head/><body><p><span style=\" font-weight:600;\">Log "
                                             "View</span></p></body></html>"))
        self.lbl_drone_info.setText(_translate("SkyRoad",
                                               "<html><head/><body><p><span style=\" font-weight:600;\">Drone "
                                               "Information</span></p></body></html>"))
        self.lbl_ip_addr.setText(_translate("SkyRoad", "접속자 IP"))
        self.lbl_drone_id.setText(_translate("SkyRoad", "드론 ID"))

    # 드론에 아이템과 hidden value 값을 추가하는 함수
    def addItem(self, drone_data):
        try:
            count = 0
            for i in range(0, 4):

                if count == 0:
                    drone_id = QtWidgets.QListWidgetItem(drone_data[2])
                    drone_id.setData(QtCore.Qt.ItemDataRole.UserRole, drone_data[2])
                    self.list_drone.addItem(drone_id)
                    count += 1

                elif count == 1:
                    user_id = QtWidgets.QListWidgetItem(drone_data[0]['user_id'])
                    user_id.setData(QtCore.Qt.ItemDataRole.UserRole, drone_data[2])
                    self.list_user_id.addItem(user_id)
                    count += 1

                elif count == 2:
                    drone_uid = QtWidgets.QListWidgetItem(str(drone_data[0]['drone_id']))
                    drone_uid.setData(QtCore.Qt.ItemDataRole.UserRole, drone_data[2])
                    self.list_drone_id.addItem(drone_uid)
                    count += 1

                elif count == 3:
                    ip_addr = QtWidgets.QListWidgetItem(drone_data[1])
                    ip_addr.setData(QtCore.Qt.ItemDataRole.UserRole, drone_data[2])
                    self.list_ip_addr.addItem(ip_addr)
                    count += 1
        except Exception as e:
            print(e)

    # item 을 삭제하는 함수
    def delete_item(self, items):
        try:

            count = 0
            for i in range(0, 4):

                if count == 0:
                    existing_items = self.list_drone.findItems(items[2], QtCore.Qt.MatchFlag.MatchExactly)
                    if existing_items:
                        item_index = self.list_drone.row(existing_items[0])
                        self.list_drone.takeItem(item_index)
                    count += 1

                elif count == 1:
                    existing_items = self.list_user_id.findItems(items[0]['user_id'], QtCore.Qt.MatchFlag.MatchExactly)
                    if existing_items:
                        item_index = self.list_user_id.row(existing_items[0])
                        self.list_user_id.takeItem(item_index)
                    count += 1

                elif count == 2:
                    existing_items = self.list_drone_id.findItems(items[0]['drone_id'], QtCore.Qt.MatchFlag.MatchExactly)
                    if existing_items:
                        item_index = self.list_drone_id.row(existing_items[0])
                        self.list_drone_id.takeItem(item_index)
                    count += 1

                elif count == 3:
                    existing_items = self.list_ip_addr.findItems(items[1], QtCore.Qt.MatchFlag.MatchExactly)
                    if existing_items:
                        item_index = self.list_ip_addr.row(existing_items[0])
                        self.list_ip_addr.takeItem(item_index)
                    count += 1
        except Exception as e:
            print(e)

    # 로그를 log_view에 추가 작업 하는 함수
    def append_log(self, _organization, log):
        try:
            self.qtext_log_view.append(f'{_organization}: {log} ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})')
        except Exception as e:
            print(e)

    # log_view의 스크롤바를 마지막으로 내리는 함수
    def set_scrollbar(self):
        try:
            scrollbar = self.qtext_log_view.verticalScrollBar()
            # scrollbar.setValue(scrollbar.maximum())

            while True:
                # 사용자가 스크롤바를 맨 밑에 뒀는지 체크
                is_scrollbar_bottom = scrollbar.value() == scrollbar.maximum()
                if 100 >= scrollbar.maximum() - scrollbar.value():
                    is_scrollbar_bottom = True

                if is_scrollbar_bottom:
                    scrollbar.setValue(scrollbar.maximum())

                time.sleep(1)

        except Exception as e:
            print(e)

    # 예외처리 or 오류 처리 함수
    def append_except_log(self, log, addr, data=None):
        try:
            self.qtext_log_view.append(f'IP : {addr}, Except Log : {log}')

            if data != None:
                self.qtext_log_view.append(f'Client Data : {data}')
        except Exception as e:
            print(e)

    # status 바를 추가하는 함수 년 월 일로 지정해놓음
    def set_status_bar(self, SkyRoad):
        try:
            status_bar = SkyRoad.statusBar()
            status_bar.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(14, 49, 104); border: 1px solid;")
            time_label = QtWidgets.QLabel()
            status_bar.addWidget(time_label)
            update_time = threading.Thread(target=self.update_time, args=(status_bar, ))
            update_time.daemon = True
            update_time.start()
        except Exception as e:
            print(e)

    # 실시간 시간을 업데이트 해주는 함수
    def update_time(self, status_bar):
        try:
            while True:
                current_time = QDateTime.currentDateTime().toString("yyyy년 MM월 dd일 hh시 mm분 ss초")
                status_bar.showMessage(current_time)
                time.sleep(1)
        except Exception as e:
            print(e)

    def clear_log_view(self):
        try:
            if not self.qtext_log_view.document().isEmpty():
                self.qtext_log_view.clear()

        except Exception as e:
            print(e)

    def update_server_obj(self, obj_server):
        self.drone_server = obj_server
        self.drone_server.update_log_view.connect(self.append_log)
        self.drone_server.update_append_except_log.connect(self.append_except_log)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SkyRoad = QtWidgets.QMainWindow()
    ui = Ui_SkyRoad(SkyRoad)
    # ui.setupUi(SkyRoad)
    SkyRoad.show()
    sys.exit(app.exec_())
