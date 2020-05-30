# -*- coding: utf-8 -*-
# Author：crx349 www.xmspace.net
# QQ:842062626

import time
import os

def get_stop_service(designation):
    """To obtain a list of running the service name,
    check whether the monitoring server is present in the list.
    """
    lines = os.popen('net start').readlines()
    line = [item.strip() for item in [i for i in lines]]
    if designation in line:
        return True
    else:
        return False
		
def main(sname):
	isDown = get_stop_service(sname)
	return isDown
	
if __name__ == '__main__':

    name = 'World Wide Web Publishing Service'
    response = main(name)
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = "iischeck_log.txt"
    file = open(f,"a")
    if response:
        file.write(str(name)+" "+str(response)+" "+str(localtime)+"\n")
    else:
	    os.system('iisreset /start')
	    file.write(str(name)+" start ok"+" "+str(localtime)+"\n")