import os
import sys
import subprocess
import platform

#static variables
EXPECTED_OS = 'Linux'
TRUSTED = 0
USERID = os.getuid()
SYSTEM = platform.system()
DISTRIBUTION = platform.linux_distribution()[0]

#pkg update for x distros
def apt_repo():
    deb_repo = subprocess.run(
        ['apt-get', 'update'],
        stdout=subprocess.PIPE
        )
    print(deb_repo.stdout.decode('utf-8'))

def dnf_repo():
    fed_repo = subprocess.run(
        ['dnf', 'update'],
        stdout=subprocess.PIPE
        )
    print(fed_repo.stdout.decode('utf-8'))

def equo_repo():
    entro_repo = subprocess.run(
        ['equo', 'up'],
        stdout=subprocess.PIPE
        )
    print(fed_repo.stdout.decode('utf-8'))

def pacman_repo():
    arch_repo = subprocess.run(
        ['pacman', '-Sy'],
        stdout=subprocess.PIPE
        )
    print(arch_repo.stdout.decode('utf-8'))

def yum_repo():
    cent_repo = subprocess.run(
        ['yum', 'update'],
        stdout=subprocess.PIPE
        )
    print(cent_repo.stdout.decode('utf-8'))

def zypper_repo():
    suse_repo = subprocess.run(
        ['zypper', 'up'],
        stdout=subprocess.PIPE
        )
    print(suse_repo.stdout.decode('utf-8'))

#pip installations for x distros
def apt_pip():
    get_pip = subprocess.run(
        ['apt', 'install', 'python3-pip'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))

def yum_pip():
    get_epel = subprocess.run(
        ['yum', 'install', 'epel-release'],
        stdout=subprocess.PIPE
        )
    print(get_epel.stdout.decode('utf-8'))
    get_pip = subprocess.run(
        ['yum', 'install', 'python-pip'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))

def dnf_pip():
    get_pip = subprocess.run(
        ['dnf', 'install', 'python3'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))

def pacman_pip():
    get_pip = subprocess.run(
        ['pacman', '-S', 'python-pip'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))

def zypper_pip():
    get_pip = subprocess.run(
        ['zypper', 'install', 'python3-pip'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))

def equo_pip():
    get_pip = subprocess.run(
        ['emerge', '--ask', 'dev-python/pip'],
        stdout=subprocess.PIPE
        )
    print(get_pip.stdout.decode('utf-8'))
    print("Be aware that running pip as root is not reccomended.")

#determine whether pip is installed or not
def pip_existence():
    if subprocess.run(['which','pip'],stdout=subprocess.PIPE).stdout.decode('utf-8') == '':
        return False
    else:
        return True

#returns true if os = linux
def required(operative_system):
    if operative_system == EXPECTED_OS:
        return True
    else:
        raise Exception("This script is intended for Linux users.")

#returns true if user is rooted
def active_permission(UID):
    if type(UID) is int:
        if UID == TRUSTED:
            return True
        else:
            return False
    else:
        raise Exception("The f is you")

#most used-distros
PKG_UPDATE = {
    'arch': pacman_repo,
    'debian': apt_repo,
    'centos': yum_repo,
    'fedora': dnf_repo,
    'SuSE': zypper_repo,
    'gentoo': equo_repo
}

PIP_INSTALL = {
    'arch': pacman_pip,
    'debian': apt_pip,
    'centos': yum_pip,
    'fedora': dnf_pip,
    'SuSE': zypper_pip,
    'gentoo': equo_pip
}

#updates packages
def update_repo():
    if DISTRIBUTION in PKG_UPDATE:
          PKG_UPDATE[DISTRIBUTION]()

#if pip ain't installed, it will be.
def pip_installer():
    if pip_existence():
        pass
    else:
        if DISTRIBUTION in PIP_INSTALL:
            PIP_INSTALL[DISTRIBUTION]()

if required(SYSTEM):
    if active_permission(USERID):
        update_repo()
        pip_installer()
else:
    sys.exit()