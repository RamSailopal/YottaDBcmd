#!/bin/bash
if [[ "$1" != "start" && "$1" != "stop" && "$1" != "status" ]]
then
	echo "Pass either start, stop or status as the first parameter"
	exit
fi
if [[ "$1" == "start" ]]
then
	if test -e yottaserver.pid
        then
		echo "Process is already running as $(cat yottaserver.pid)"
		exit
	fi
	nohup ./yottacmd-server </dev/null >/dev/null 2>&1 &
	echo $! > yottaserver.pid

elif [[ "$1" == "stop" ]]
then
	if test -e yottaserver.pid
        then
		kill -9 $(cat yottaserver.pid)
                rm -f yottaserver.pid
	else
		echo "Process is not running!!"
		exit
	fi
elif [[ "$1" == "status" ]]
then
        if test -e yottaserver.pid
        then
                echo "Process is running as process $(cat yottaserver.pid)"
		exit
        else
                echo "Process is not running!!"
                exit
        fi
fi

