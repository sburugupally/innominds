import os
import sys
import subprocess

def command_exe(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    process.wait()
    print(str(out.decode('ascii')))

command_exe("git clone https://github.com/sburugupally/innominds.git")
os.chdir("C:/Users/sburugupally/Downloads/git_project/git_package/shoot")
