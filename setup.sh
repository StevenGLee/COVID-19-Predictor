#!/bin/bash
#apt install pip3
pip install -r requirements.txt
CRTDIR=$(pwd)
TIMECMD="0 15 * * * root"
PYFILENAME="/daily_routine.py"
ADDLINE="${TIMECMD} ${CRTDIR}${PYFILENAME}"
if cat '/etc/crontab' | grep "$PYFILENAME" > /dev/null
then
	sed -i "$PYFILENAME"'/d' /etc/crontab
fi
echo "$ADDLINE" >> /etc/crontab	
