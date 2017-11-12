# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#


import os
from  pcmd.env import Env


# conf/zhi_miner.ini
class ParaCmdEnv(Env):
    HOME_KEY = 'PARACMD_HOME'
    CONF_FILE = 'conf/paracmd.ini'

    def __init__(self):
        super(ParaCmdEnv, self).__init__(homeKey=ParaCmdEnv.HOME_KEY)
        self.load(file=ParaCmdEnv.CONF_FILE, relative=True)
        userConfFile = self.getConfItem(section='misc', option='user_conf')
        userHome = os.environ.get('HOME')
        userConfFile = userHome + '/' + userConfFile
        #print 'Path of user conf file: ' + userConfFile
        self.load(file=userConfFile, relative=False)




