# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#

import redis
from pcmd.env_pc import ParaCmdEnv

class DataConn(object):
    def __init__(self):
        self.env = ParaCmdEnv.GetInstance()
        self.conn = redis.StrictRedis(host='mu01', port=6379, db=0, password='sider')

    def getConn(self):
        return self.conn

    def set(self, key, val):
        return self.conn.set(key, val)

    def get(self, key):
        return self.conn.get(key)
 
