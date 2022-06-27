import os
import subprocess

# define return value
SUCCESS_CODE = 0
ERROR_CODE = -1


# export Domain GPO applies to computer
def export_domain_gpo():
    # get temp path dir
    curr_path_dir = os.getcwd()
    temp_gpo_path_file = curr_path_dir + "\\temp\\gpo_apply.xml"

    try:
        # update config gpo/policy
        cmd = "gpupdate /force"
        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if len(output.stderr):
            print("Error: Can't update gpo applies to computer")
            return ERROR_CODE

        # export gpo to xml file
        cmd = "gpresult /x " + temp_gpo_path_file + " /F"
        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if len(output.stderr):
            print("Error: Can't export gpo applies to computer")
            print(output.stderr)
            return ERROR_CODE
        return SUCCESS_CODE
    except Exception as e:
        print(e)
        return ERROR_CODE


# main func
if __name__ == "__main__":
    export_domain_gpo()
