# Metasploit-Armitage-Installer-Ubuntu
Metasploit and Armitage installer for Ubuntu 16.04 


# Install Ruby Like So...
    curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
    curl -L https://get.rvm.io | bash -s stable
    source /etc/profile.d/rvm.sh
    echo "source /etc/profile.d/rvm.sh" >> ~/.bashrc
    
    source ~/.bashrc
    RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
    rvm install $RUBYVERSION
    rvm use $RUBYVERSION --default
    ruby -v
    
# Then Simply Run
    python3 setup.py
    
# Next
     cat database.yml > /opt/metasploit-framework/config/database.yml
     sh -c "echo export MSF_DATABASE_CONFIG=/opt/metasploit-framework/config/database.yml >> /etc/profile"
     source /etc/profile
     su postgres    
     createuser msf -P -S -R -D
     createdb -O msf msf
     exit
 
# Finally
     you will need to reboot your machine/vm 
     first start the postgresql database by issuing "service postgresql restart"
     then start metasploit by issuing "msfconsole"
     after that you can access armitage by issuing "armitage" and changing the password on the ui to msf. :)
