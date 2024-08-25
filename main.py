from datetime import datetime
import subprocess
import time
# sp.run(["ls -al | grep ENSE"])

# Run the command
# result = subprocess.run('ls -al | grep ENSE', shell=True,) # stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# result = subprocess.run('rclone sync ~/obdsidian/Kaiomurz/ googledrive:/DriveSyncFiles/Kaiomurz', shell=True,) # stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
while True:
    subprocess.run('rclone sync ~/obdsidian/Kaiomurz/ googledrive:/DriveSyncFiles/Kaiomurz', shell=True,) # stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(datetime.now())
    time.sleep(10)
# Get the output
# output = result.stdout

# Print the output
# print(output, time.time()-start)

# rclone sync ~/obdsidian/Kaiomurz/ googledrive:/DriveSyncFiles/Kaiomurz