import subprocess

def execute_shell_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print (str(out.decode('ascii')))
    print(str(error.decode('ascii')))
    pipe.wait()

def git_clone(repo_dir='C:/Users\sburugupally\Downloads\drone'):
    cmd = 'git clone ' + 'https://github.com/mpigelati/Python_adb'+' '+ repo_dir
    execute_shell_command(cmd)


git_clone()
