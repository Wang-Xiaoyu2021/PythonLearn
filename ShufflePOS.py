#!/usr/bin/env python
# rundom occupation site shuffle script wrote by Aaron Wang

import numpy as np 
import csv
import random
#data = []
infile_path = 'POSCAR'
outfile_path = 'POSCAR_Shuffle'
def ShufflePOS(data):
    #data = []
    natoms = []

    # 读取输入POSCAR文件所有内容
    with open(infile_path, encoding = 'utf-8',) as POSCAR:
        line = POSCAR.readlines()
        for i,rows in enumerate(line):
            if i in range(0,len(line)):
                #print(rows.strip())        # str.strip()去掉首位空格回车等字符
                data.append(rows)
    print("length",len(data))
    POSCAR.close()

    # print(list(enumerate(line))) # Debug
    # 读取分数占据元素位置数量
    for i,rows in enumerate(line):
        if i == 6:
            for j in rows.split():         # str.split()按照空格分割字符串为列表
                natoms.append(int(j))
            nsites = sum(natoms[0:2])
            #print(sum(natoms))
            #print(sum(rows[0:-3].split()))
            #print(list(rows[0:-1]))
    print('total random sites:',nsites)

    # 生成随机排序随机原子位置，并链接成新POSCAR
    rand_list = data[8:8+nsites]
    random.shuffle(rand_list)
    #print(rand_list)  # Debug
    data = data[0:8] + rand_list + data[8+nsites:]
    return(data)

def GeneryPOSCAR():
    #print(data)
    # 写生出来的新的POSCAR
    for i in range(10):
        data = []
        lines = ShufflePOS(data)
        with open(outfile_path + str(i), "w",) as f:
            for i in range(len(lines)):
                f.writelines(lines[i])
        f.close()

if __name__ == "__main__":
    GeneryPOSCAR()