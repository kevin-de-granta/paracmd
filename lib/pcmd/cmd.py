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
from pcmd.env_pc import ParaCmdEnv

class Command(object):
    def __init__(self, val=None, token=None, type='query', id=None, cmdPkg=None):
        """
        Command types:
            query/cap(ture):  to call with os.popen(to capture the output)
            sub/subprocess[optional]: to call with subprocess.popen, for more interaction.
            sys/silent:    to call with system(start a new process)(with no output and zero control)
            intr:   internal command of ParamCmd.
            dynamic:    commands dynamically loaded.
        Command Package:
            a string with command value/string, type, and other info packed in.
        """
        self.conf = dict()
        self.conf['sys-token'] = token
        self.conf['cmd-id'] = id # TODO: generate one if None
        self.conf['cmd-content'] = content
        self.conf['cmd-type'] = type

    def toStr(self):
        return str(self.conf)

    def execute(self):
        pass



