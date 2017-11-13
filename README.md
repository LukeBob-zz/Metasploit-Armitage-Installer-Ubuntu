# Metasploit-Armitage-Installer-Ubuntu-Debian
metasploit and armitage installer for ubuntu 16.04 and debian based distros
# WARNING NOT TESTED!!!!

# Install Ruby Like So...
    curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
    curl -L https://get.rvm.io | bash -s stable
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
