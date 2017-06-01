#!/usr/bin/python
import os
import sys
import time
import unittest

from daemon import Daemon


class CronjobCheckDaemon(Daemon):
    def __init__(self, *args, **kwargs):
        super(CronjobCheckDaemon, self).__init__(*args, **kwargs)
        testoutput = open('cronjob_check_daemon.txt', 'a')
        testoutput.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': inited\n')
        testoutput.close()

    def run(self):
	while 1:
            testoutput = open('cronjob_check_daemon.txt', 'a')
            processNumber = os.popen("ps aux | grep 'cronjob.php' | grep -v 'grep'|wc -l").read()
            #testoutput.write(processNumber)
            if(int(processNumber) < 1):
                testoutput.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': process is not running, restart\n')
                pid = os.popen("/usr/bin/php cronjob.php &").read()
                #testoutput.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': pid:' + pid + '\n')
            time.sleep(1)
            testoutput.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ('start', 'stop', 'restart'):
            d = CronjobCheckDaemon('cronjob_check_daemon.pid', verbose=0)
            #d.run()
            getattr(d, arg)()
