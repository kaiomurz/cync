import subprocess

# sp.run(["ls -al | grep ENSE"])

# Run the command
result = subprocess.run('ls -al | grep ENSE', shell=True,) # stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output
output = result.stdout

# Print the output
print(output)

# rclone sync ~/obdsidian/Kaiomurz/ googledrive:/DriveSyncFiles/Kaiomurz