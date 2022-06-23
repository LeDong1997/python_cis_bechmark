import os
import subprocess


# export Domain GPO applies to computer
def export_domain_gpo():
    path_dir = os.getcwd()
    print(path_dir)

    # try:
    #     cmd = "gpresult /x gporeport1.xml /F"
    #     # command = "gpresult /H dong1.html"
    #     # output = subprocess.run(command, shell=True, capture_output=True, text=True)
    #     output = subprocess.run(command, shell=True, capture_output=True, text=True)
    #     print(output.stdout)
    #     # print(output.stderr)
    # except ValueError:
    #     print("abc")


# main func
if __name__ == "__main__":
    export_domain_gpo()
