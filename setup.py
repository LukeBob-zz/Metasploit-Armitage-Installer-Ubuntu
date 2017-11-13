## Author: Luke Bob
##
## information gathered from https://www.darkoperator.com/installing-metasploit-in-ubunt/
##

#!/usr/bin/python3
import os
import time

Cur_Dir = __file__

def Install_Java():
    print("\n\t Installing Java\n\n")
    time.sleep(2)
    repo = """
    add-apt-repository -y ppa:webupd8team/java
    apt-get update
    apt-get -y install oracle-java8-installer
    """
    os.system(repo)
    print("\n\t Java Installed\n\n")
    time.sleep(2)    

def Install_Dependencys():
    print("\n\t Installing Dependencys\n\n")
    time.sleep(2)
    Deps = """
    apt-get update
    apt-get -y upgrade
    apt-get -y install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev vncviewer libyaml-dev curl zlib1g-dev
    """
    os.system(Deps)
    print("\n\t Dependencys Installed\n\n")
    time.sleep(2)

def Install_Ruby():
    print("\n\t Installing Ruby\n\n")
    time.sleep(2)
    Rub = """
    curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
    curl -L https://get.rvm.io | bash -s stable 
    """
    Rub1= """
    source /etc/profile.d/rvm.sh
    echo 'source /etc/profile.d/rvm.sh' >> ~/.bashrc
    source ~/.bashrc
    RUBYVERSION=2.4.2
    rvm use $RUBYVERSION --default
    ruby -v
    """
    
    os.system(Rub)
    time.sleep(1) ## Debugging purposes
    os.system(Rub1)
    print("\n\tRuby Installed\n")
    time.sleep(2)

def Install_Nmap():
    print("\n\tInstalling Nmap\n\n")
    time.sleep(2)
    nm = """
    mkdir ~/Development
    cd ~/Development
    git clone https://github.com/nmap/nmap.git
    cd nmap
    ./configure
    make
    make install
    make clean
    """

    os.system(nm)
    print("\n\tInstalled Nmap\n\n")
    time.sleep(2)

def Configure_Postgresql():
    print("\n\t Configuring Postgresql For Metasploit\n\n")
    time.sleep(2)
    post = """
    su postgres
    createuser msf -P -S -R -D
    createdb -O msf msf
    """

    os.system(post)
    print("\nPostgresql Configured\n\n")
    time.sleep(2)

def Install_Metasploit():
    print("\n\tInstalling Metasploit Framework\n\n")
    time.sleep(2)
    meta = """
    cd /opt
    git clone https://github.com/rapid7/metasploit-framework.git
    chown -R root /opt/metasploit-framework
    cd metasploit-framework
    rvm --default use ruby-${RUBYVERSION}@metasploit-framework
    gem install bundler
    bundle install
    bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
    """

    os.system(meta)
    print("\n\t Installed Metasploit Framework\n\n")
    time.sleep(2)


def Install_Armitage():
    print("\n\t Installing Armitage\n\n")
    time.sleep(2)
    armit = """
    curl -# -o /tmp/armitage.tgz http://www.fastandeasyhacking.com/download/armitage150813.tgz
    tar -xvzf /tmp/armitage.tgz -C /opt
    ln -s /opt/armitage/armitage /usr/local/bin/armitage
    ln -s /opt/armitage/teamserver /usr/local/bin/teamserver
    sh -c 'echo java -jar /opt/armitage/armitage.jar \$\* > /opt/armitage/armitage'
    perl -pi -e 's/armitage.jar/\/opt\/armitage\/armitage.jar/g' /opt/armitage/teamserver
    touch /opt/metasploit-framework/config/database.yml
    """
    os.system(armit)
    dir_path = os.path.dirname(os.realpath(Cur_Dir))
    chdir = "cd {0}".format(dir_path)

    cet   = """
    cat database.yml > /opt/metasploit-framework/config/database.yml
    sh -c 'echo export MSF_DATABASE_CONFIG=/opt/metasploit-framework/config/database.yml >> /etc/profile'
    source /etc/profile
    """
    os.system(chdir)
    os.system(cet)
    print("\n\t Armitage Installed\n")
    time.sleep(2)

def main():
    try:
        Install_Java()
        Install_Dependencys()
        Install_Ruby()
        Install_Nmap() 
        Install_Metasploit()
        Configure_Postgresql()
        Install_Armitage()
    except: raise
    exit(0)

    os.system("msfconsole")
    time.sleep(5)
    os.system("exit")
    print("\n\tDefault Armitage User:msf Pass:msf\n\n")
    print("\n\t Metasploit-Framework\n\t Successfully Installed\n\t System Needs To Be Rebooted\n")


if __name__ == '__main__':
    main()
