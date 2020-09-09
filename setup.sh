#!/bin/bash
apt install pip3 git
pip3 install gitpython
git clone https://github.com/CSSEGISandData/COVID-19.git ./data
CRTDIR=$(pwd)
TIMECMD="0 15 * * * root"
PYFILENAME="/daily_routine.py"
ADDLINE="${TIMECMD} ${CRTDIR}${PYFILENAME}"
if cat '/etc/crontab' | grep "$PYFILENAME" > /dev/null
then
	sed -i "$PYFILENAME"'/d' /etc/crontab
fi
echo "$ADDLINE" >> /etc/crontab	
