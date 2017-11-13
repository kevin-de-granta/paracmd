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
from pcmd.daemon import Daemon
from pcmd.master import Master
from pcmd.slave import Slave

class DaemonFactory:
    def __init__(self):
        pass

    @staticmethod
    def MakeDaemon():
        env = ParaCmdEnv.GetInstance()
        daemon = None
        thisHost = os.environ.get('HOSTNAME')
        if(thisHost=='mu01'):
            daemon = Master()
        else:
            daemon = Slave()
        return daemon

