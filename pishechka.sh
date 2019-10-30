#!/bin/bash
# /etc/init.d/pishechka.sh
### BEGIN INIT INFO
# Provides:				pishechka.sh
# Required-Start:		$remote_fs $syslog
# Required-Stop:		$remote_fs $syslog
# Default-Start:		2 3 4 5
# Default-Stop:			0 1 6
# Short-Description:	Start video at boot time
# Description:			Open videoplaying program at boot time.
### END INIT INFO
sudo python3 /opt/pishechka_videoplay/program.py
