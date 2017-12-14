import FreeCAD, FreeCADGui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportMesh.ui'
#
# Created: Thu Dec 07 22:06:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(QtGui.QDialog):
    def __init__(self, currentObj):
        QtGui.QDialog.__init__(self)
        self.setupUi(currentObj)
    def setupUi(self, currentObj):
        self.obj = currentObj
        self.setObjectName("Dialog")
        self.resize(360, 180)
        #self.tabWidget = QtGui.QTabWidget(self)
        #self.tabWidget.setGeometry(QtCore.QRect(10, 20, 361, 211))
        #font = QtGui.QFont()
        #font.setFamily("Helvetica")
        #self.tabWidget.setFont(font)
        #self.tabWidget.setObjectName("tabWidget")
        #self.tab = QtGui.QWidget()
        #self.tab.setObjectName("tab")
        #self.conductorBox = QtGui.QDialogButtonBox(self.tab)
        #self.conductorBox.setGeometry(QtCore.QRect(190, 150, 156, 23))
        #self.conductorBox.setOrientation(QtCore.Qt.Horizontal)
        #self.conductorBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        #self.conductorBox.setObjectName("conductorBox")
        #self.label_3 = QtGui.QLabel(self.tab)
        #self.label_3.setGeometry(QtCore.QRect(20, 20, 161, 41))
        #font = QtGui.QFont()
        #font.setFamily("Helvetica")
        #self.label_3.setFont(font)
        #self.label_3.setObjectName("label_3")
        self.surroundingPermBox = QtGui.QDoubleSpinBox(self)
        self.surroundingPermBox.setGeometry(QtCore.QRect(240, 30, 101, 21))
        self.surroundingPermBox.setObjectName("surroundingPermBox")
        #self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtGui.QWidget()
        #self.tab_2.setObjectName("tab_2")
        self.dielectricBox = QtGui.QDialogButtonBox(self)
        self.dielectricBox.setGeometry(QtCore.QRect(190, 150, 156, 23))
        self.dielectricBox.setOrientation(QtCore.Qt.Horizontal)
        self.dielectricBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dielectricBox.setObjectName("dielectricBox")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.innerPermBox = QtGui.QDoubleSpinBox(self)
        self.innerPermBox.setGeometry(QtCore.QRect(240, 30, 101, 21))
        self.innerPermBox.setObjectName("innerPermBox")
        self.outerPermBox = QtGui.QDoubleSpinBox(self)
        self.outerPermBox.setGeometry(QtCore.QRect(240, 90, 101, 21))
        self.outerPermBox.setObjectName("outerPermBox")
        #self.tabWidget.addTab(self.tab_2, "")
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 232, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi()
        #self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.dielectricBox, QtCore.SIGNAL("accepted()"), self.create_interface)
        #QtCore.QObject.connect(self.conductorBox, QtCore.SIGNAL("accepted()"), self.create_conductor_interface)
        # Todo: change this btw
        QtCore.QObject.connect(self.dielectricBox, QtCore.SIGNAL("rejected()"), self.hide)
        #QtCore.QObject.connect(self.conductorBox, QtCore.SIGNAL("rejected()"), self.hide)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Dialog", "Current object: " + self.obj, None, QtGui.QApplication.UnicodeUTF8))
        #self.label_3.setText(QtGui.QApplication.translate("Dialog", "Surrounding surface permitivity", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Conductor Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Innner surface permitivity:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Outer surface permitivity:", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Dielectric Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", self.obj, None, QtGui.QApplication.UnicodeUTF8))

    def create_interface(self):
        self.inperm = self.innerPermBox.value()
        self.outperm = self.outerPermBox.value()
        self.isConductor = False
        self.accept()
#Todo: Dialog closes immediately open being opened - garbage collected?
#Might need to redesign as one class, instead of the UI being a member object of meshCreator
