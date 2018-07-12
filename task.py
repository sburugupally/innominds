import os
import sys
import subprocess


def command_exe(cmd):
 process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
 out, err = process.communicate()
 process.wait()
 print(str(out.decode('ascii')))

############################
# command_exe("mkdir python_hub")
# command_exe("cd python_hub")
# str="all files are added"
command_exe('git clone git@github.com:mpigelati/Python_adb.git')
# os.system('git log --pretty=format:"%h - %an, %ar : %s')
# command_exe("git reset --hard origin/master")
os.chdir("C:/Users\sburugupally\Downloads\drone")
#command_exe(" git log>log_info.json")

