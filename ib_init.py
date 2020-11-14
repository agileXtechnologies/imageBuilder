import subprocess, os, time, pyfiglet, platform
#yum conf docker
def confYum():
    os.system('echo "[dockerrepo]" > /etc/yum.repos.d/docker.repo')
    os.system('echo "enabled=1" >> /etc/yum.repos.d/docker.repo')
    os.system('echo "name=docker" >> /etc/yum.repos.d/docker.repo')
    os.system('echo "baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/" >> /etc/yum.repos.d/docker.repo')
    os.system('echo "gpgcheck=0" >> /etc/yum.repos.d/docker.repo')
    os.system("yum install docker-ce --nobest -y")
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
    print("If you have system with yum, you don't have to worry about docker installation.")
    print("If you don't have it, do install docker & git in your system.")
    print("-------------------------------------------------------------------")
    if input("Press q to exit or any key to continue") == "q":
        exit() 
    else:
        pass
    print("[*] configure system")
    if subprocess.getstatusoutput("docker version")[0] != 0: 
        print("[*] need to install docker")
        confYum()
        print("[✔] docker installed")
    os.system("yum install git -y")
    if input("[*] press y if you have hub.docker.com account else any key to continue") == "y":
        os.system("docker login")
    else:
        pass
    print("[*] configuring language classifier")
    os.system("docker build -t linguist .")
    print("[✔] configured language classifier")
    print("[✔] configured system")


