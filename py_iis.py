# -*- coding:utf-8 -*-
# Author：crx349 www.xmspace.net
# QQ:842062626

import time 
import psutil
import os
 
def getcpu():
    cpu_percent = psutil.cpu_percent(interval=10,percpu=False)
    return cpu_percent
 
def restart_iis():
    cpu_percent = getcpu()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = "cpu_log.txt"
    file = open(f,"a")
    file.write(str(cpu_percent)+" "+str(localtime)+"\n")
    #print (cpu_percent)
    if cpu_percent > 80:
        os.system('iisreset /restart')
        file.write(str(cpu_percent)+" restart ok"+"\n")
 
if __name__ == '__main__':
    restart_iis()