# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterName.ui'
#
# Created: Wed Dec 13 15:42:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(329, 186)
        self.groupName = QtGui.QLineEdit(self)
        self.groupName.setGeometry(QtCore.QRect(172, 70, 141, 20))
        self.groupName.setObjectName("groupName")
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(160, 150, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 70, 161, 21))
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.saveName)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.hide)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Group Naming", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Enter name of group:", None, QtGui.QApplication.UnicodeUTF8))

    def saveName(self):
        self.groupName = self.groupName.displayText()
        self.accept()