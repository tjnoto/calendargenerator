# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumy.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sumy(object):
    def setupUi(self, Sumy):
        Sumy.setObjectName("Sumy")
        Sumy.resize(621, 233)
        self.gridLayoutWidget = QtWidgets.QWidget(Sumy)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 601, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 601, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.filepath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.filepath.setObjectName("filepath")
        self.horizontalLayout_2.addWidget(self.filepath)
        self.browse = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.browse.setObjectName("browse")
        self.horizontalLayout_2.addWidget(self.browse)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 601, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.all = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.all.setObjectName("all")
        self.horizontalLayout.addWidget(self.all)
        self.current = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.current.setObjectName("current")
        self.horizontalLayout.addWidget(self.current)
        self.nextmonth = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.nextmonth.setObjectName("nextmonth")
        self.horizontalLayout.addWidget(self.nextmonth)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 601, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.info = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.info.setObjectName("info")
        self.horizontalLayout_3.addWidget(self.info)
        self.submit = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.submit.setObjectName("submit")
        self.horizontalLayout_3.addWidget(self.submit)
        self.quit = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.quit.setObjectName("quit")
        self.horizontalLayout_3.addWidget(self.quit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Sumy)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 199, 601, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.retranslateUi(Sumy)
        QtCore.QMetaObject.connectSlotsByName(Sumy)
        Sumy.setTabOrder(self.filepath, self.browse)

    def retranslateUi(self, Sumy):
        _translate = QtCore.QCoreApplication.translate
        Sumy.setWindowTitle(_translate("Sumy", "Dialog"))
        self.label.setText(_translate("Sumy", "Spreadsheet:"))
        self.browse.setText(_translate("Sumy", "Browse"))
        self.label_2.setText(_translate("Sumy", "Month(s):"))
        self.all.setText(_translate("Sumy", "A&ll"))
        self.current.setText(_translate("Sumy", "&Current"))
        self.nextmonth.setText(_translate("Sumy", "Ne&xt"))
        self.label_6.setText(_translate("Sumy", "WARNING!  THIS WILL ONLY WORK WITH SPECIALLY FORMATTED SPREADSHEETS!"))
        self.info.setText(_translate("Sumy", "Info"))
        self.submit.setText(_translate("Sumy", "Create Schedule"))
        self.quit.setText(_translate("Sumy", "Quit"))
        self.label_5.setText(_translate("Sumy", "Made for: Wayne Romeo"))
        self.label_3.setText(_translate("Sumy", "CALENDAR GENERATOR"))
        self.label_4.setText(_translate("Sumy", "vBETA"))
