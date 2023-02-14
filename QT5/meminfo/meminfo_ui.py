#!/usr/bin/python3
import sys
import fileinput
import csv
import numpy as np
import re
import matplotlib.pyplot as plt
from time import strptime
import time
import meminfo_qt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

fiels = ["time", "MemFree", "MemAvailable", "Buffers", "Cached", "Active", "Inactive",
"Active\(anon\)", "Inactive\(anon\)", "Active\(file\)", "Inactive\(file\)", "Unevictable", "Mlocked",
"SwapFree", "Dirty", "Writeback", "AnonPages", "Mapped", "Shmem", "Slab", "SReclaimable", 
"SUnreclaim", "KernelStack", "PageTables", "NFS_Unstable", "Bounce", "WritebackTmp", "CommitLimit", 
"Committed_AS", "VmallocTotal", "VmallocUsed", "VmallocChunk", "Percpu", "CmaTotal", "CmaFree"]

fiels_flags = meminfo_qt5.fiels_flags

def usage():
    print("usage:%s filename"%sys.argv[0])

def log2csv():
    global ui
    filename = ui.file_input.log_file
    print("filename=%s"%filename)
    if filename == "":
        print("Please select file first.\n")

    with open("%s.csv"%filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fiels)
        writer.writeheader()
        info={}
        info["time"] = "1"

        res = []
        for i in range(1, len(fiels)):
            patter = "%s:[ ]+(.+?) kB"%fiels[i]
            res.append(re.compile(patter))
        print(res)
        try: 
            for line in fileinput.input(filename):
                for i in range(1, len(fiels)):
                    patter = res[i-1]
                    value = patter.findall(line)
                    if value:
                        info[fiels[i]] = value[0]
                        if i == (len(fiels) - 1):
                            # 2023-02-10 21:17:46
                            # time_tmp = re.findall(r"^\[(.+?)\]", line)
                            # if time_tmp:
                            #     time_tmp = strptime(time_tmp[0], "%Y-%m-%d %H:%M:%S")
                            #     time_tmp = time.mktime(time_tmp)
                            #     info[fiels[0]] = int(time_tmp)
                                # print(time_tmp)
                            writer.writerow(info)
                        break
                        
                # value = re.findall(r"MemFree:[ ]+(.+?) kB", line)
                # if value:
                #     info["MemFree"] = value[0]
                #     print("MemFree=%s"%value[0])
                #     continue
        except:
            print("AN ERROR")

    msg_box = QMessageBox(QMessageBox.Information, 'Load', 'Load finish')
    msg_box.exec_()

def draw():
    global ui
    filename = ui.file_input.log_file
    filename = "%s.csv"%filename

    meminfo = np.loadtxt(filename, dtype=np.int64, delimiter=",", skiprows=1)
    print(meminfo)
    print(meminfo[:, 1])
    x = np.array(range(0,meminfo.shape[0]))

    for i in range(0, len(fiels)):
        if fiels_flags[fiels[i]]:
            y = meminfo[:,i]
            plt.plot(x, y, label=fiels[i])

    plt.legend()
    plt.xlabel('time')
    plt.ylabel('kB')
    plt.show()

def check_box_changed(check_box):
    global MainWindow
    print(check_box)
    check_box = MainWindow.findChild(QtWidgets.QCheckBox, check_box)
    print(check_box.isChecked())
    box_name = check_box.objectName()
    print(box_name)
    if box_name == "Active_anon":
        fiels_flags["Active\(anon\)"] = check_box.isChecked()
    elif box_name == "Inactive_anon":
        fiels_flags["Inactive\(anon\)"] = check_box.isChecked()
    elif box_name == "Active_file":
        fiels_flags["Active\(file\)"] = check_box.isChecked()
    elif box_name == "Inactive\(file\)":
        fiels_flags["Inactive\(file\)"] = check_box.isChecked()
    else:
        fiels_flags[box_name] = check_box.isChecked()

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     usage()
    #     exit(0)
    # print(sys.argv)
    # log2csv(sys.argv[1])
    # draw("%s.csv"%sys.argv[1])

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = meminfo_qt5.Ui_Dialog()
    ui.setupUi(MainWindow)

    for i in range(1, len(fiels)):
        if fiels[i] == "Active\(anon\)":
            check_box = MainWindow.findChild(QtWidgets.QCheckBox, "Active_anon")
            if fiels_flags[fiels[i]]:
                check_box.setChecked(True)
        elif fiels[i] == "Inactive\(anon\)":
            check_box = MainWindow.findChild(QtWidgets.QCheckBox, "Inactive_anon")
            if fiels_flags[fiels[i]]:
                check_box.setChecked(True)
        elif fiels[i] == "Active\(file\)":
            check_box = MainWindow.findChild(QtWidgets.QCheckBox, "Active_file")
            if fiels_flags[fiels[i]]:
                check_box.setChecked(True)
        elif fiels[i] == "Inactive\(file\)":
            check_box = MainWindow.findChild(QtWidgets.QCheckBox, "Inactive_file")
            if fiels_flags[fiels[i]]:
                check_box.setChecked(True)
        else:
            check_box = MainWindow.findChild(QtWidgets.QCheckBox, fiels[i])
            if fiels_flags[fiels[i]]:
                check_box.setChecked(True)

    ui.Load.clicked.connect(log2csv)
    ui.Reflush.clicked.connect(draw)

    MainWindow.show()

    sys.exit(app.exec_())
