# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#


from pcmd.daemon import Daemon

class Slave(Daemon):
    def __init__(self, *args, **kwargs):
        super(Slave, self).__init__(*args, **kwargs)

    def serve(self, *args, **kwargs):
	super(Slave, self).serve(self, *args, **kwargs)
