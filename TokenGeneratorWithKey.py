# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:40:03 2016

@author: pingxin.zhang
"""
import binascii
import vipaccess.utils as vipaccess

request = vipaccess.generate_request()
response = vipaccess.get_provisioning_response(request)

otp_token = vipaccess.get_token_from_response(response.content)

otp_secret = vipaccess.decrypt_key(otp_token['iv'], otp_token['cipher'])

print 'TOKEN-ID: %s'%(otp_token['id'])
print 'TOKEN-Key: %s'%(binascii.b2a_hex(otp_secret).decode('utf-8'))

#print otp_token