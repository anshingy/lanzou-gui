# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rach/Documents/lanzou-gui/share.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 310)
        Dialog.setMinimumSize(QtCore.QSize(340, 260))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.out_layout = QtWidgets.QVBoxLayout()
        self.out_layout.setObjectName("out_layout")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setObjectName("logo")
        self.out_layout.addWidget(self.logo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_name = QtWidgets.QLabel(Dialog)
        self.lb_name.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_name.setObjectName("lb_name")
        self.verticalLayout.addWidget(self.lb_name)
        self.lb_size = QtWidgets.QLabel(Dialog)
        self.lb_size.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_size.setObjectName("lb_size")
        self.verticalLayout.addWidget(self.lb_size)
        self.lb_time = QtWidgets.QLabel(Dialog)
        self.lb_time.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_time.setObjectName("lb_time")
        self.verticalLayout.addWidget(self.lb_time)
        self.lb_dl_count = QtWidgets.QLabel(Dialog)
        self.lb_dl_count.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_dl_count.setObjectName("lb_dl_count")
        self.verticalLayout.addWidget(self.lb_dl_count)
        self.lb_share_url = QtWidgets.QLabel(Dialog)
        self.lb_share_url.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_share_url.setObjectName("lb_share_url")
        self.verticalLayout.addWidget(self.lb_share_url)
        self.lb_pwd = QtWidgets.QLabel(Dialog)
        self.lb_pwd.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_pwd.setObjectName("lb_pwd")
        self.verticalLayout.addWidget(self.lb_pwd)
        self.lb_dl_link = QtWidgets.QLabel(Dialog)
        self.lb_dl_link.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.lb_dl_link.setObjectName("lb_dl_link")
        self.verticalLayout.addWidget(self.lb_dl_link)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.tx_share_url = QtWidgets.QLineEdit(Dialog)
        self.tx_share_url.setObjectName("tx_share_url")
        self.gridLayout.addWidget(self.tx_share_url, 5, 0, 1, 1)
        self.tx_time = QtWidgets.QLabel(Dialog)
        self.tx_time.setText("")
        self.tx_time.setObjectName("tx_time")
        self.gridLayout.addWidget(self.tx_time, 3, 0, 1, 1)
        self.tx_size = QtWidgets.QLabel(Dialog)
        self.tx_size.setText("")
        self.tx_size.setObjectName("tx_size")
        self.gridLayout.addWidget(self.tx_size, 1, 0, 1, 1)
        self.tx_name = QtWidgets.QLineEdit(Dialog)
        self.tx_name.setObjectName("tx_name")
        self.gridLayout.addWidget(self.tx_name, 0, 0, 1, 1)
        self.tx_dl_link = QtWidgets.QTextBrowser(Dialog)
        self.tx_dl_link.setObjectName("tx_dl_link")
        self.gridLayout.addWidget(self.tx_dl_link, 8, 0, 1, 1)
        self.tx_dl_count = QtWidgets.QLabel(Dialog)
        self.tx_dl_count.setText("")
        self.tx_dl_count.setObjectName("tx_dl_count")
        self.gridLayout.addWidget(self.tx_dl_count, 4, 0, 1, 1)
        self.tx_pwd = QtWidgets.QLineEdit(Dialog)
        self.tx_pwd.setObjectName("tx_pwd")
        self.gridLayout.addWidget(self.tx_pwd, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.out_layout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.out_layout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.out_layout)
        self.lb_name.setBuddy(self.tx_name)
        self.lb_share_url.setBuddy(self.tx_share_url)
        self.lb_pwd.setBuddy(self.tx_pwd)
        self.lb_dl_link.setBuddy(self.tx_dl_link)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logo.setText(_translate("Dialog", "TextLabel"))
        self.lb_name.setText(_translate("Dialog", "文件名："))
        self.lb_size.setText(_translate("Dialog", "文件大小："))
        self.lb_time.setText(_translate("Dialog", "上传时间："))
        self.lb_dl_count.setText(_translate("Dialog", "下载次数："))
        self.lb_share_url.setText(_translate("Dialog", "分享链接："))
        self.lb_pwd.setText(_translate("Dialog", "提取码："))
        self.lb_dl_link.setText(_translate("Dialog", "下载直链："))
