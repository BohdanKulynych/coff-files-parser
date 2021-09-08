import subprocess
import os


def modify_txt(filename:str):
    file = open(filename).readlines()
    with open(filename, "w") as F:
        F.writelines(file[10:-2])

def extract_object_filenames(path:str):
    for file in os.listdir(path):
        if file.endswith(".obj"):
            print(file)


def read_coff_files(path:str, filename:str):
    f = open(filename, "w")
    process = subprocess.Popen("cmd", shell=True, stdin=subprocess.PIPE, stdout=f)
    path_to_dumpbin = r"cd C:\Program Files (x86)\Microsoft Visual " \
                      r"Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64" + "\n "
    process.stdin.write(path_to_dumpbin.encode())
    path_to_coff = rf"dumpbin /ALL {path}\*.obj" + "\n"
    process.stdin.write(path_to_coff.encode())
    process.communicate()
    f.close()
    modify_txt(filename)


if __name__ == "__main__":
    path = r"C:\Users\Bohdan_Kulynych\source\repos\lab2_pdc\lab2_pdc\Debug"
    print(f"Filenames located by {path} and  will be composed into .dll library")
    extract_object_filenames(path)

    read_coff_files(path,"out.txt")
