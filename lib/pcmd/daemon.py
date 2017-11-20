# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#

import os
import sys
import time
import datetime
from pcmd.util import DataConn

class Daemon(object):
    sleep_duration=1

    def __init__(self, *args, **kwargs):
        self.hostname=os.environ.get('HOSTNAME')
        self.hbKey='heart-beat-' + self.hostname #heart beat
        self.cmdKey='cmd-to-' + self.hostname
        self.replyKey='reply-from-' + self.hostname
        appHome = os.environ.get('PARACMD_HOME')
        self.intrptFileGlobal = appHome + '/tmp/intrpt/pdaemon.global'
        self.intrptFileLocal = appHome + '/tmp/intrpt/pdaemon.' + self.hostname + '.local'
        print self.intrptFileGlobal
        print self.intrptFileLocal
        self.conn = DataConn()

    def serve(self, *args, **kwargs):
        while True:
            currTime = str(datetime.datetime.now())
            rtVal = self.conn.set(self.hbKey, currTime)
            # print 'Updating heart beat: ' + self.hbKey + ' => ' + currTime + ' => ' + str(rtVal)
            cmd = self.conn.get(self.cmdKey)
            self.conn.delete(self.cmdKey)
            # DONE: then delete the pair (self.cmdKey, cmd) in the memory DB.
            if cmd is not None:
                print 'Running command: \"' + cmd + '\"'
                outLines = os.popen(cmd)
                lineList = []
                for line in outLines:
                    line = line.strip()
                    lineList.append(line)
                reply = '\n'.join(lineList)
                self.conn.set(self.replyKey, reply)
            if(os.path.exists(self.intrptFileGlobal) or os.path.exists(self.intrptFileGlobal)):
                # break # ?
                sys.exit(0)
            time.sleep(Daemon.sleep_duration)

if __name__ == '__main__':
    print("Hello")

