!#/bin/bash

su postgres
echo "Creating User msf"
createuser msf -P -S -R -D
echo "Creating Database msf With Password msf"
createdb -O msf msf
