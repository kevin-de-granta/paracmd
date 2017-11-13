# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#

import os
from pcmd.env_pc import ParaCmdEnv
from pcmd.util import DataConn

class Client(object):
    #
    def __init__(self):
        self.env = ParaCmdEnv.GetInstance()
        self.conn = DataConn()

    def qHBeat(self):
        # ConfigParser only supports lowwer-case letters, while domainname of s191 (TS10K) is in upper-case. ==> take care of it.
        nodeStr = self.env.get('clusters', 'ts10k')
        print 'Processing node string: ' + nodeStr
        nodeNameList = nodeStr.split(',')
        for node in nodeNameList:
            hbName = 'heart-beat-' + node
            print hbName
            heartBeat = self.conn.get(hbName)
            if heartBeat is not None:
                print str(node) + ': ' + heartBeat
