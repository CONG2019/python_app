# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meminfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import os

fiels_flags = {
    "time": 0,
    "MemFree": 0,
    "MemAvailable": 0,
    "Buffers": 0,
    "Cached": 0,
    "Active": 0,
    "Inactive": 0,
    "Active\(anon\)": 0,
    "Inactive\(anon\)": 0,
    "Active\(file\)": 0,
    "Inactive\(file\)": 0,
    "Unevictable": 0,
    "Mlocked": 0,
    "SwapFree": 0,
    "Dirty": 0,
    "Writeback": 0,
    "AnonPages": 0,
    "Mapped": 0,
    "Shmem": 0,
    "Slab": 1,
    "SReclaimable": 0,
    "SUnreclaim": 1,
    "KernelStack": 0,
    "PageTables": 0,
    "NFS_Unstable": 0,
    "Bounce": 0,
    "WritebackTmp": 0,
    "CommitLimit": 0,
    "Committed_AS": 0,
    "VmallocTotal": 0,
    "VmallocUsed": 0,
    "VmallocChunk": 0,
    "Percpu": 0,
    "CmaTotal": 0,
    "CmaFree": 0
}

class file_obj(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(file_obj, self).__init__(parent)
        self.clicked.connect(self.file)
        self.log_file = "";

    def file(self):
        filename = QFileDialog.getOpenFileNames(self, 'file input', os.getcwd(), "All Files(*);;Text Files(*.txt)")
        print(filename[0][0])
        self.log_file = filename[0][0]

class my_check_box(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        super(my_check_box, self).__init__(parent)
        self.stateChanged.connect(self.box_changed)

    def box_changed(self):
        global fiels_flags
        box_name = self.objectName()
        print(box_name)
        if box_name == "Active_anon":
            fiels_flags["Active\(anon\)"] = self.isChecked()
        elif box_name == "Inactive_anon":
            fiels_flags["Inactive\(anon\)"] = self.isChecked()
        elif box_name == "Active_file":
            fiels_flags["Active\(file\)"] = self.isChecked()
        elif box_name == "Inactive_file":
            fiels_flags["Inactive\(file\)"] = self.isChecked()
        else:
            fiels_flags[box_name] = self.isChecked()
            print(fiels_flags[box_name])


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1006, 741)
        

        self.file_input = file_obj(Dialog)
        self.file_input.setGeometry(QtCore.QRect(500, 650, 131, 61))
        self.file_input.setObjectName("file_input")

        self.Load = QtWidgets.QPushButton(Dialog)
        self.Load.setGeometry(QtCore.QRect(670, 650, 131, 61))
        self.Load.setObjectName("Load")
        self.Reflush = QtWidgets.QPushButton(Dialog)
        self.Reflush.setGeometry(QtCore.QRect(840, 650, 131, 61))
        self.Reflush.setObjectName("Reflush")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 481, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.MemAvailable = my_check_box(self.formLayoutWidget)
        self.MemAvailable.setObjectName("MemAvailable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.MemAvailable)
        self.Inactive = my_check_box(self.formLayoutWidget)
        self.Inactive.setObjectName("Inactive")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Inactive)
        self.MemFree = my_check_box(self.formLayoutWidget)
        self.MemFree.setAcceptDrops(False)
        self.MemFree.setObjectName("MemFree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.MemFree)
        self.Active_anon = my_check_box(self.formLayoutWidget)
        self.Active_anon.setObjectName("Active_anon")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Active_anon)
        self.Buffers = my_check_box(self.formLayoutWidget)
        self.Buffers.setObjectName("Buffers")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Buffers)
        self.Inactive_anon = my_check_box(self.formLayoutWidget)
        self.Inactive_anon.setObjectName("Inactive_anon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Inactive_anon)
        self.Cached = my_check_box(self.formLayoutWidget)
        self.Cached.setObjectName("Cached")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Cached)
        self.Active_file = my_check_box(self.formLayoutWidget)
        self.Active_file.setObjectName("Active_file")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Active_file)
        self.Active = my_check_box(self.formLayoutWidget)
        self.Active.setObjectName("Active")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Active)
        self.Inactive_file = my_check_box(self.formLayoutWidget)
        self.Inactive_file.setObjectName("Inactive_file")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Inactive_file)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(490, 10, 481, 291))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setSpacing(8)
        self.formLayout_3.setObjectName("formLayout_3")
        self.Unevictable = my_check_box(self.formLayoutWidget_2)
        self.Unevictable.setObjectName("Unevictable")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Unevictable)
        self.AnonPages = my_check_box(self.formLayoutWidget_2)
        self.AnonPages.setObjectName("AnonPages")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.AnonPages)
        self.Mlocked = my_check_box(self.formLayoutWidget_2)
        self.Mlocked.setAcceptDrops(False)
        self.Mlocked.setObjectName("Mlocked")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Mlocked)
        self.Mapped = my_check_box(self.formLayoutWidget_2)
        self.Mapped.setObjectName("Mapped")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Mapped)
        self.SwapFree = my_check_box(self.formLayoutWidget_2)
        self.SwapFree.setObjectName("SwapFree")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.SwapFree)
        self.Shmem = my_check_box(self.formLayoutWidget_2)
        self.Shmem.setObjectName("Shmem")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Shmem)
        self.Dirty = my_check_box(self.formLayoutWidget_2)
        self.Dirty.setObjectName("Dirty")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Dirty)
        self.Slab = my_check_box(self.formLayoutWidget_2)
        self.Slab.setObjectName("Slab")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Slab)
        self.Writeback = my_check_box(self.formLayoutWidget_2)
        self.Writeback.setObjectName("Writeback")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Writeback)
        self.SReclaimable = my_check_box(self.formLayoutWidget_2)
        self.SReclaimable.setObjectName("SReclaimable")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SReclaimable)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 320, 481, 291))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(8)
        self.formLayout_4.setObjectName("formLayout_4")
        self.SUnreclaim = my_check_box(self.formLayoutWidget_3)
        self.SUnreclaim.setObjectName("SUnreclaim")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SUnreclaim)
        self.WritebackTmp = my_check_box(self.formLayoutWidget_3)
        self.WritebackTmp.setObjectName("WritebackTmp")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.WritebackTmp)
        self.KernelStack = my_check_box(self.formLayoutWidget_3)
        self.KernelStack.setAcceptDrops(False)
        self.KernelStack.setObjectName("KernelStack")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.KernelStack)
        self.CommitLimit = my_check_box(self.formLayoutWidget_3)
        self.CommitLimit.setObjectName("CommitLimit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CommitLimit)
        self.PageTables = my_check_box(self.formLayoutWidget_3)
        self.PageTables.setObjectName("PageTables")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PageTables)
        self.Committed_AS = my_check_box(self.formLayoutWidget_3)
        self.Committed_AS.setObjectName("Committed_AS")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Committed_AS)
        self.NFS_Unstable = my_check_box(self.formLayoutWidget_3)
        self.NFS_Unstable.setObjectName("NFS_Unstable")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.NFS_Unstable)
        self.VmallocTotal = my_check_box(self.formLayoutWidget_3)
        self.VmallocTotal.setObjectName("VmallocTotal")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.VmallocTotal)
        self.Bounce = my_check_box(self.formLayoutWidget_3)
        self.Bounce.setObjectName("Bounce")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Bounce)
        self.VmallocUsed = my_check_box(self.formLayoutWidget_3)
        self.VmallocUsed.setObjectName("VmallocUsed")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.VmallocUsed)
        self.formLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(490, 320, 481, 291))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setSpacing(8)
        self.formLayout_5.setObjectName("formLayout_5")
        self.VmallocChunk = my_check_box(self.formLayoutWidget_4)
        self.VmallocChunk.setObjectName("VmallocChunk")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.VmallocChunk)
        self.Percpu = my_check_box(self.formLayoutWidget_4)
        self.Percpu.setAcceptDrops(False)
        self.Percpu.setObjectName("Percpu")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Percpu)
        self.CmaFree = my_check_box(self.formLayoutWidget_4)
        self.CmaFree.setObjectName("CmaFree")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.CmaFree)
        self.CmaTotal = my_check_box(self.formLayoutWidget_4)
        self.CmaTotal.setObjectName("CmaTotal")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CmaTotal)
        self.kdialog = QtWidgets.QDialog(Dialog)
        self.kdialog.setGeometry(QtCore.QRect(90, 680, 16, 16))
        self.kdialog.setObjectName("kdialog")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.file_input.setText(_translate("Dialog", "File"))
        self.Load.setText(_translate("Dialog", "Load"))
        self.Reflush.setText(_translate("Dialog", "Reflush"))
        self.MemAvailable.setText(_translate("Dialog", "MemAvailable"))
        self.Inactive.setText(_translate("Dialog", "Inactive"))
        self.MemFree.setText(_translate("Dialog", "MemFree"))
        self.Active_anon.setText(_translate("Dialog", "Active(anon)"))
        self.Buffers.setText(_translate("Dialog", "Buffers"))
        self.Inactive_anon.setText(_translate("Dialog", "Inactive(anon)"))
        self.Cached.setText(_translate("Dialog", "Cached"))
        self.Active_file.setText(_translate("Dialog", "Active(file)"))
        self.Active.setText(_translate("Dialog", "Active"))
        self.Inactive_file.setText(_translate("Dialog", "Inactive(file)"))
        self.Unevictable.setText(_translate("Dialog", "Unevictable"))
        self.AnonPages.setText(_translate("Dialog", "AnonPages"))
        self.Mlocked.setText(_translate("Dialog", "Mlocked"))
        self.Mapped.setText(_translate("Dialog", "Mapped"))
        self.SwapFree.setText(_translate("Dialog", "SwapFree"))
        self.Shmem.setText(_translate("Dialog", "Shmem"))
        self.Dirty.setText(_translate("Dialog", "Dirty"))
        self.Slab.setText(_translate("Dialog", "Slab"))
        self.Writeback.setText(_translate("Dialog", "Writeback"))
        self.SReclaimable.setText(_translate("Dialog", "SReclaimable"))
        self.SUnreclaim.setText(_translate("Dialog", "SUnreclaim"))
        self.WritebackTmp.setText(_translate("Dialog", "WritebackTmp"))
        self.KernelStack.setText(_translate("Dialog", "KernelStack"))
        self.CommitLimit.setText(_translate("Dialog", "CommitLimit"))
        self.PageTables.setText(_translate("Dialog", "PageTables"))
        self.Committed_AS.setText(_translate("Dialog", "Committed_AS"))
        self.NFS_Unstable.setText(_translate("Dialog", "NFS_Unstable"))
        self.VmallocTotal.setText(_translate("Dialog", "VmallocTotal"))
        self.Bounce.setText(_translate("Dialog", "Bounce"))
        self.VmallocUsed.setText(_translate("Dialog", "VmallocUsed"))
        self.VmallocChunk.setText(_translate("Dialog", "VmallocChunk"))
        self.Percpu.setText(_translate("Dialog", "Percpu"))
        self.CmaFree.setText(_translate("Dialog", "CmaFree"))
        self.CmaTotal.setText(_translate("Dialog", "CmaTotal"))