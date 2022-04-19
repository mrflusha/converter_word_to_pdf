import os
import subprocess
import sys



def new_del(path_to):
    path_to = path_to.replace("\\","/")
    print(path_to)
        
    dirname = path_to
    filename = "~*"
    pathname = os.path.abspath(os.path.join(dirname, filename))
    print(pathname)
    os.remove(pathname)


def convert(path, path_to):
	cv_shell = subprocess.Popen("docto.exe -f \"" + path + "\" -O \"" + path_to + "\" -T wdFormatPDF  -OX .pdf", stdout=subprocess.PIPE, encoding='Windows-1251', shell=False)
	out = cv_shell.stdout.read()
	return out


def del_temp(path_to):
    print(path_to)
    try:
        path_to = path_to.replace("\\","/")
        path_to = os.path.abspath(os.path.join(path_to, "~*"))
        print(path_to)

        del_str = f"del {path_to}"
        print(del_str)
        subprocess.Popen(del_str, stdout=subprocess.PIPE, encoding='Windows-1251', shell=True)
        #subprocess.Popen(del_str, stdout=subprocess.PIPE, encoding='Windows-1251', shell=True)

    except OSError as e:
        print(e)




