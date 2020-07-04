import os
import glob
import datetime
import shutil
import re
import sys
from functools import cmp_to_key
from pathlib import Path
def get_dirs(path):
   
    files = os.listdir(path)
    dirs=[]
    for file in files:
            dirs.append(file)
    print(dirs)
    return dirs

def comp(x, y):
    # x_number = re.search("([0-9]*).ts",x,0).group(1)
    # y_number = re.search("([0-9]*).ts",y,0).group(1)
    x_number = int(re.search("([0-9]*).ts",x,0).group(1))
    y_number = int(re.search("([0-9]*).ts",y,0).group(1))
    if x_number > y_number:
        return 1
    if x_number < y_number:
        return -1
    return 0
    
""" def split_str(name):
    name = name.split("_")[-1]
    name = name[3:]
    path_name = dir+name """
# 执行子文件夹内所有文件ts文件重命名
def rename(dir_path):
    print('rename')
    # 目录判定
    if Path(dir_path).is_dir() == False:
        return
    filelist = os.listdir(dir_path)
    print(filelist)
    counter = 0
    for item in filelist:
        # 已重命名则跳过
        result = re.search("^([0-9]*).ts",item,0)
        if result:
            break
        #set the old file name 
        if item.split(".")[1] == "ts":
            # print(item)
            # print(filelist[counter])
            oldname = dir_path + r"\\" + filelist[counter]
            #set the new file name 
            # newname = dir_path + r"\\" + str(counter) + "." + item.split("jpg")[2].split(".")[1]
            # name_ = re.search("mid([0-9]*)",item,0).group(1)
            name_ = re.search("low([0-9]*)",item,0).group(1)
            newname = dir_path + r"\\" + str(name_) + ".ts" 

            print(oldname)
            print(newname)
            #write the resolution information to the file
            #rename the file
            os.rename(oldname, newname)
            #print oldname , newname
            #write the width and height to the posf file
        counter += 1
        

def ts2mp4(dir,path):
    # 重写文件名
    mp4=dir+'.mp4'
    dir=path+dir+"/"
    rename(dir)
    print(dir)
    time = datetime.datetime.now()
    list_ts = []
    list_ts = glob.glob(dir+"*.ts")
    list_ts.sort(key=cmp_to_key(comp))
    print('++++++')
    print(list_ts)
    # print(list_ts)
    ts_number=len(list_ts)


    cmd='copy /b '
    # print(cmd)
    cmd_ = ''
    for index,i in enumerate(list_ts):
        if index!=ts_number-1:
            cmd_ += i + '+'
        else:
            cmd_ += i
    cmd_ = cmd_.replace("/","\\")
    cmd=cmd + cmd_ +' '+dir.replace("/","\\")+'new.gen'
    print(cmd)
    os.system(cmd)
    print('2')
    cmd = 'ffmpeg -i '+dir+'new.gen -c copy '+'./test/output/'+mp4
    print(cmd)
    os.system(cmd)
    #shutil.copy(dir+mp4,"./test/output"+mp4)
    print("done")
    
if __name__=='__main__':
    path="./123/"
    dirs=get_dirs(path)
    number=0
    print(dirs)
    for dir in dirs:
        # 判断目录
        if Path(path+dir).is_dir() == False:
            break
        # 目录为输出目录跳出判定
        if dir == "output":
            break
        ts2mp4(dir,path)
        number+=1
    print("共转换完成{}个视频".format(number))
    