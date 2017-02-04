# AutoAnyConnectScipt
A script to automate connect to Cisco AnyConnect with second authorized security code with Symantec VIP Access.
# Usage
$python AutoAnyConnectScript.py your_config_file.json

It will toggle between connect/disconnect VPN with this command.

# Dependences 
- python 2.7.3
- oath
- json

# Notes
Before you can use this script to login your VPN automatically, you should register a new credential ID from Symantec and get the ID's secret key. I use the python-vipaccess to register a new credential ID and get its secret key. Here are 2 references I searched from Google:
- https://github.com/cyrozap/python-vipaccess
- https://gist.github.com/p120ph37/8213727

After you register your credential ID and get the ID's secret key, you can fill in the user_profile_config_template.json (I just use plaintext to store it in my case, you can encrypt it or use other method to store it, as it contains many sensitive account information) and use this configure file to login your VPN. Enjoy it.
