#!/usr/bin/python3
import sys
import fileinput
import csv
import numpy as np
import re
import matplotlib.pyplot as plt
from time import strptime
import time

fiels = ["time", "MemFree", "MemAvailable", "Buffers", "Cached", "Active", "Inactive",
"Active\(anon\)", "Inactive\(anon\)", "Active\(file\)", "Inactive\(file\)", "Unevictable", "Mlocked",
"SwapFree", "Dirty", "Writeback", "AnonPages", "Mapped", "Shmem", "Slab", "SReclaimable", 
"SUnreclaim", "KernelStack", "PageTables", "NFS_Unstable", "Bounce", "WritebackTmp", "CommitLimit", 
"Committed_AS", "VmallocTotal", "VmallocUsed", "VmallocChunk", "Percpu", "CmaTotal", "CmaFree"]

fiels_flags = {
    "time": 0,
    "MemFree": 1,
    "MemAvailable": 0,
    "Buffers": 0,
    "Cached": 0,
    "Active": 0,
    "Inactive": 0,
    "Active\(anon\)": 0,
    "Inactive\(anon\)": 0,
    "Active\(file\)": 0,
    "Inactive\(file\)": 0,
    "Unevictable": 1,
    "Mlocked": 0,
    "SwapFree": 0,
    "Dirty": 0,
    "Writeback": 0,
    "AnonPages": 0,
    "Mapped": 0,
    "Shmem": 0,
    "Slab": 1,
    "SReclaimable": 1,
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

def usage():
    print("usage:%s [-l] filename"%sys.argv[0])

def log2csv(filename):
    print("filename=%s"%filename)
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
        #try: 
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
                            #     # print(time_tmp)
                        writer.writerow(info)
                    break
                    
            # value = re.findall(r"MemFree:[ ]+(.+?) kB", line)
            # if value:
            #     info["MemFree"] = value[0]
            #     print("MemFree=%s"%value[0])
            #     continue
        #except:
        #    print("AN ERROR")

def draw(filename):
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

if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
        usage()
        exit(0)
    print(sys.argv)
    if sys.argv[1] == "-l":
        log2csv(sys.argv[len(sys.argv) - 1])

    draw("%s.csv"%sys.argv[len(sys.argv) - 1])
