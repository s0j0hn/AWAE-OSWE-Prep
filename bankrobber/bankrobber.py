import sys
import threading
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

parser = argparse.ArgumentParser(description='XSS => SQi => RCE (Bankrobber hackthebox)')

parser.add_argument("--targetIp", default=None, type=str, help="Bankrobber ip address")
parser.add_argument("--localIp", default=None, type=str, help="Your IP address")
args = parser.parse_args()

# def get_command():
#     try:
#         # cmd = input(':\> ')
#         # t = threading.Thread(target=send_command, args=())
#         # t.start()
#     except:
#         sys.exit(0)


def send_command(cmd):
    global target_url, local_url


class MyServer(HTTPServer):
    def server_activate(self):
        # get first command
        # get_command()
        HTTPServer.server_activate(self)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_request(self, *argus, **kwargs):
        return

    def log_message(self, *argus, **kwargs):
        return

    def do_GET(self):
        global query_id
        self.send_error(404)


if __name__ == '__main__':
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
