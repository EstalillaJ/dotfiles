import subprocess
import os
import shutil

def CreateSwitchCase(cases, blocks):
    case = {}
    for idx, case in enumerate(cases):
        case[case] = blocks[idx]
    return case

def Apt-Get(package):
    command = "apt-get -y install %s" % (package)
    bash(command)

# Debian package installer
def Dpkg(package):
    command = "dpkg -i %s" % (package)
    bash(command)

# Atom Package Manager
def Apm(package):
    command = "apm install %s" % (package)
    bash(command)

def Install(program, softwareToDownload):

    installers = ["apt-get", "apm", "dpkg"]
    blocks = [Apt-Get, Apm, Dpkg]
    case = CreateSwitchCase(installers, blocks)

    case[program](softwareToDownload)

def bash(command):
    subprocess.call(["sudo"] + command.split())

def Main():
    scriptDir = os.path.dirname(__file__)
    homeDir = os.path.expanduser("~")

    # add keys for spotify, mono, etc
    print "adding ppas"
    keys = open(os.path.join(scriptDir, "apt-get/keys")).readlines()
    for command in keys:
        bash(command)

    print  "installing apt-get packages"
    aptGetPackages = open(os.path.join(scriptDir,"apt-get/apt-get.packages")).readlines()
    for package in aptGetPackages:
        Apt-Get(package)

    print "installing apm packages"
    apmPackages = open(os.path.join(scriptDir, "apm/apm.packages")).readlines()
    for package in apmPackages:
        Apm(package)

    # install misc (fonts, etc)
    misc = open(os.path.join(scriptDir, "misc/commands")).readlines()
    for command in misc:
        bash(command)

    configDir = os.path.join(homeDir, ".config")
    toStow = [name for name in os.listdir(scriptDir) if os.path.isdir(os.path.join(scriptDir, name))]
    for line in toStow:
        if os.path.exists(os.path.join(homeDir,line[line.find("/")+1:])):
            shutil.rmtree(os.path.join(homeDir,line[line.find("/")+1:]))
        bash("stow " + line[:line.find("/")])
    # stow configs
    print "removing unneeded packages"
    #remove unneeded packages
    bash("apt auto-remove")



if __name__=='__main__':
    main()
