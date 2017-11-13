## Author: Luke Bob
##
## information gathered from https://www.darkoperator.com/installing-metasploit-in-ubunt/
##

#!/usr/bin/python3
import os
import time


def Install_Java():
    print("\n\t [#] Installing Java [#]\n\n")
    time.sleep(2)
    repo = """
    add-apt-repository -y ppa:webupd8team/java
    apt-get update
    apt-get -y install oracle-java8-installer
    """
    os.system(repo)
    print("\n\t [#] Java Installed [#]\n\n")
    time.sleep(2)    

def Install_Dependencys():
    print("\n\t [#] Installing Dependencys [#]\n\n")
    time.sleep(2)
    Deps = """
    apt-get update
    apt-get -y upgrade
    apt-get -y install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev vncviewer libyaml-dev curl zlib1g-dev
    """
    os.system(Deps)
    print("\n\t [#] Dependencys Installed [#]\n\n")
    time.sleep(2)

def Install_Ruby():
    print("\n\t [#] Installing Ruby [#]\n\n")
    time.sleep(2)
  
    
    Rub = """
    cd ~
    git clone git://github.com/sstephenson/rbenv.git .rbenv
   echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    exec $SHELL

    git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
    echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc

  
    git clone git://github.com/dcarley/rbenv-sudo.git ~/.rbenv/plugins/rbenv-sudo

    exec $SHELL

    RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
    rbenv install $RUBYVERSION
    rbenv global $RUBYVERSION
    ruby -v
    """
  
    os.system(Rub)
    print("\n\t [#] Ruby Installed [#]\n\n")
    time.sleep(2)

def Install_Nmap():
    print("\n\t [#] Installing Nmap [#]\n\n")
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
    print("\n\t [#] Installed Nmap [#]\n\n")
    time.sleep(2)


def Install_Metasploit():
    print("\n\t [#] Installing Metasploit Framework [#]\n\n")
    time.sleep(2)
    meta = """
    cd /opt
    git clone https://github.com/rapid7/metasploit-framework.git
    chown -R root /opt/metasploit-framework
    cd metasploit-framework
    rvm --default use ruby-2.4.2@metasploit-framework
    gem install bundler
    bundle install
    bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
    """

    os.system(meta)
    print("\n\t [#] Installed Metasploit Framework [#]\n\n")
    time.sleep(2)


def Install_Armitage():
    print("\n\t [#] Installing Armitage [#]\n\n")
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

    cet   = """
    cat database.yml > /opt/metasploit-framework/config/database.yml
    sh -c 'echo export MSF_DATABASE_CONFIG=/opt/metasploit-framework/config/database.yml >> /etc/profile'
    source /etc/profile
    """
    os.system(cet)
    print("\n\t [#] Armitage Installed [#]\n\n")
    time.sleep(2)

def main():
    try:
        Install_Java()
        Install_Dependencys()
        Install_Ruby()
        Install_Nmap() 
        Install_Metasploit()
        #Configure_Postgresql()
        Install_Armitage()
    except: raise
    exit(0)

    os.system("msfconsole")
    time.sleep(5)
    os.system("exit")
    print("\n\tDefault Armitage User:msf Pass:msf\n")
    print("\n\tDONT FORGET TO RUN bash postg.sh or Metasploit wont be able to connect to the database!!!\n\n")
    print("\n\t Metasploit-Framework\n\t Successfully Installed\n\t System Needs To Be Rebooted\n")


if __name__ == '__main__':
    main()
