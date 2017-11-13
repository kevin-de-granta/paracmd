# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#

import os
import time
import datetime
from pcmd.util import DataConn

class Daemon(object):
    sleep_duration=2

    def __init__(self, *args, **kwargs):
        self.hostname=os.environ.get('HOSTNAME')
        self.hbKey='heart-beat-' + self.hostname #heart beat
        self.cmdKey='cmd-to-' + self.hostname
        self.replyKey='reply-from-' + self.hostname
        self.conn = DataConn()

    def serve(self, *args, **kwargs):
        while True:
            currTime = str(datetime.datetime.now())
            rtVal = self.conn.set(self.hbKey, currTime)
            print 'Updating heart beat: ' + self.hbKey + ' => ' + currTime + ' => ' + str(rtVal)
            time.sleep(Daemon.sleep_duration)
        pass

if __name__ == '__main__':
    print("Hello")

