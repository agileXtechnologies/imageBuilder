import subprocess, os, platform, pyfiglet

def ibTool():
   if platform.system() == "Windows":
      os.system("cls")
   else:
      os.system("clear")
   print("-------------------------------------------------------------------")
   ascii_banner = pyfiglet.figlet_format("imgbuild\nImage Builder")
   print(ascii_banner)
   print("-------------------------------------------------------------------")
   gitUrl= input("[.] Enter the git repo link: ")
   gitRepo= input("[.] Enter the repo name: ")
   gitClone= subprocess.getstatusoutput("git clone {0}".format(gitUrl))

