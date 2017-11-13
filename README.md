# Metasploit-Armitage-Installer-Ubuntu-Debian
metasploit and armitage installer for ubuntu 16.04 and debian based distros
# WARNING NOT TESTED!!!!

# Install Ruby Like So...
    gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
    apt-get install curl
    curl -sSL https://get.rvm.io -o rvm.sh
    cat rvm.sh | bash -s stable
    source ~/.rvm/scripts/rvm
    echo "source ~/.rvm/scripts/rvm" >> ~/.bashrc
    source ~/.bashrc
    RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
    rvm install $RUBYVERSION
    rvm use $RUBYVERSION --default
    ruby -v
    
# Simply Run
    python3 setup.py
    bash postg.sh
