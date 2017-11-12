# -*- coding:utf-8 -*-

#
# File Name:    TestEnvPC.py
# Function:     To test ParaCmd Env.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   2017/08/12
# Revised hist: revised by _____ on ____/__/__
#


from pcmd.env_pc import ParaCmdEnv


if __name__ == '__main__':
    print 'Tesing env of Para Cmd...'
    env = ParaCmdEnv()
    env.showAllConf()


