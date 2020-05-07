import sys,os
import subprocess
import pexpect
from pexpect import popen_spawn


def create_vitrual_environment(path="/",name="env"):
     arg="python -m venv "+str(name)
    #execute the command
    pass
def activate_virtual_environment(name="env"):
    activate=".\\"+str(name)+"\\Scripts\\activate"  
      #execute the command
    pass
def deactivate_virtual_environment(parameter_list):
    deactivate="deactivate"  
      #execute the command
    pass
def heroku_login(email,password):
    # import subprocess
    args = ["heroku","login","-i"]
    child_proccess = subprocess.Popen(args, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    t=email.encode()
    child_proccess.stdin.write(t)
    t=password.encode()
    child_proccess.stdin.write(t)
    child_process_output = child_proccess.communicate()[0]

    child_proccess.stdin.close()

    print(child_process_output)
    return 
def test(email,password):
    cmd='heroku login -i'
    # child = spawnu(cmd)
    process = subprocess.Popen(cmd,shell=False,bufsize=0,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # child.expect(r"(?:Email :)|(?:(?:Email\ )(?:\[)?(?:.+)(?:\])?:)")
    # child.sendline(email)
    # child.expect ('Password:')
    # child.sendline (password)
    output = terminated_read(process.stdout, "\n?")
    print(output.strip())

    print('Left interactve mode.')
    pass
def execute(command):
    subprocess.check_call(command, stdout=sys.stdout, stderr=subprocess.STDOUT)

if __name__ == "__main__":
    email="sharathkumardaroor@gmail.com"
    password="V0icem@il"
    # print(execute(["heroku", "login"]))
    print(test(email,password))

