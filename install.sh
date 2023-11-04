#!/usr/bin/bash
pathFile="HackPortsScanner" 
pkg install python
cd ~/../usr/bin 
# команда
touch attackbots
echo "cd ~/$pathFile/ && python HackPortsScanner.py" >  HackPortsScanner
chmod +x attackbots
cd ~/
#конец