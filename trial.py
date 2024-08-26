import subprocess
import time
import hashlib


def consistent_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


result = subprocess.Popen('ls -al', shell=True, stdout=subprocess.PIPE)
output = str(result.stdout.read())
print(output)
print(hashlib.sha256(output.encode('utf-8')).hexdigest())
