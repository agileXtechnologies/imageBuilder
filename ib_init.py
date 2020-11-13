import subprocess, os, time, pyfiglet, platform
    
#setup environment
def ibInit():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("-------------------------------------------------------------------")
    ascii_banner = pyfiglet.figlet_format("imgbuild\nImage Builder")
    print(ascii_banner)
    print("Source-to-Image (S2I) CLI tool focusing on Docker.\nIt is under constant development.")
    print("-------------------------------------------------------------------")
    print("[*] configure system")
    
    

ibInit()