# -*- coding:utf-8 -*-

#
# File Name:    TestCmd.py
# Function:     To test class Command.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   2017/08/12
# Revised hist: revised by _____ on ____/__/__
#


from pcmd.env_pc import ParaCmdEnv
from pcmd.cmd import Command

if __name__ == '__main__':
    print 'Tesing class Command...'
    env = ParaCmdEnv()
    env.showAllConf()


