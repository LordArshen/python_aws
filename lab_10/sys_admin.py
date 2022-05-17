#use of os and subprocess library 
import os
import subprocess
""" You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes. The subprocess.run() function can take many new arguments, but those additional arguments are optional. 
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
"""

os.system("ls")
subprocess.run(["ls"])
subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])

print("-"*20)
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("-"*20)

command="ps"
commandArgument="-s"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])