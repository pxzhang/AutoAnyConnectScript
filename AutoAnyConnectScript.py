# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:07:24 2016

@author: pxzhang409@gmail.com
"""
import json
import oath
import os
import re
import sys
from subprocess import Popen, PIPE

def load_config(config_file):
    config_dict = {}
    if not os.path.isfile(config_file):
        return config_dict
    else:
        with open(config_file, 'rb') as fd:
            config_dict = json.load(fd)
    return config_dict

def connect(conn_config_dict):
   '''
   Test the status of AnyConnect and connect to VPN if the status==Disconnected
   '''
   if 'VPNCLI_PATH' not in conn_config_dict or 'VPN_URL' not in conn_config_dict or 'USER_NAME' not in conn_config_dict or 'PASS_WD' not in conn_config_dict or 'TOKEN_KEY' not in conn_config_dict:
       print 'Invalid configure file'
       return
   state_pattern = re.compile(r'Disconnected|Connected')
   
   VPNCLI_PATH = conn_config_dict['VPNCLI_PATH']
   USER_NAME = conn_config_dict['USER_NAME']
   PASS_WD = conn_config_dict['PASS_WD']
   VPN_URL = conn_config_dict['VPN_URL']
   TOKEN_KEY = conn_config_dict['TOKEN_KEY']
   
   st_output = Popen([VPNCLI_PATH, '-s'], stdin=PIPE, stdout=PIPE).communicate(os.linesep.join(['state']))[0]
   st_output = st_output.replace('\r','')
   st_set = set(state_pattern.findall(st_output))
   conn_status = 'Disconnected'
   
   if not st_set and len(st_set) > 1:
       ### exit in case have more than one status, which means there is some issues with extract status code
       print st_output
       return False
   elif len(st_set) == 1:
       conn_status = st_set.pop()
   
   if conn_status == 'Disconnected':
       proc = Popen([VPNCLI_PATH, '-s'], stdin=PIPE, stdout=None)
       proc.communicate(os.linesep.join(['connect %s'%(VPN_URL), USER_NAME, PASS_WD, oath.totp(TOKEN_KEY), 'y']))
   elif conn_status == 'Connected':
       print st_output

if __name__ == '__main__':
   if len(sys.argv) < 1:
       print 'Usage: AutoAnyConnect.py config_file'
       sys.exit(0)
   config_file = sys.argv[1]
   config_dict = load_config(config_file)
   connect(config_dict)
