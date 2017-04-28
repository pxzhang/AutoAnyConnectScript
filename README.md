# AutoAnyConnectScipt
A script to automate connect to Cisco AnyConnect with second authorized security code with Symantec VIP Access.
# Usage
Generate token with keys with command (need to install python-vipaccess firstly):
$python TokenGeneratorWithKey.py

After generated the token with key, copy the TOKEN_ID and TOKEN_KEY to your configure file (make sure put it in a security place). Then register the TOKEN_ID with your VPN provider if you are required. 

If you are required to provide the security code in registering the TOKEN_ID, you can use oathtool in linux by:

$ oathtool --totp $key_plain

$ python AutoAnyConnectScript.py your_config_file.json

It will toggle between connect/disconnect VPN with this command.

# Dependences 
- python 2.7.3
- oath
- json
- python-vipaccess (if need to use TokenGeneratorWithKey.py)

# Notes
Before you can use this script to login your VPN automatically, you should register a new credential ID from Symantec and get the ID's secret key. I use the python-vipaccess to register a new credential ID and get its secret key. Here are 2 references I searched from Google:
- https://github.com/cyrozap/python-vipaccess
- https://gist.github.com/p120ph37/8213727

After you register your credential ID and get the ID's secret key, you can fill in the user_profile_config_template.json (I just use plaintext to store it in my case, you can encrypt it or use other method to store it, as it contains many sensitive account information) and use this configure file to login your VPN. Enjoy it.
