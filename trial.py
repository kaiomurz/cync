import subprocess
import time
import hashlib


def consistent_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# test
result = subprocess.Popen('ls -al', shell=True, stdout=subprocess.PIPE)
output = str(result.stdout.read())
print(consistent_hash(output))
print(output)

# for i in range(10):
#     result = subprocess.run('ls -al', shell=True,)
#     print(consistent_hash(str(result)))
#     time.sleep(1)

#sdfsdfsdfs