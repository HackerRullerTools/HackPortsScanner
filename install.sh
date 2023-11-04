#!/usr/bin/bash
pathFile="HackPortsScanner" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackPortsScanner
echo "cd ~/$pathFile/ && python HackPortsScanner.py" >  HackPortsScanner
chmod +x HackPortsScanner
cd ~/
#конец
