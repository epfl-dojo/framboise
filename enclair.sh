#!/bin/bash
#
# A bash script to connect to EPFL enclair portal
#
# Usage:
#	 ./enclair --connect
#	 ./enclair --connect password
#	 ./enclair --disconnect

# set +e -x

# Create the curl cmd with the password (inline or prompt)
connect() {
	curl -d "provider=epfl&login=x-rpis&password=$1&check=on" https://enclair.epfl.ch/login.php
	ping=$(ping -c 3 www.epfl.ch | grep '3 received'| cut -d ' ' -f 1)
	if [ ! -z "$ping" ]
	then
		if [ "$ping" == 3 ]
		then
			echo "You are connected."
		else 
			echo "Pings failed. Please check your password...."
		fi
	else
		echo "Connection failed. Please check your password...."
	fi
}

# Use the enclair disconnect URL aka back.php
disconnect() {
	curl https://enclair.epfl.ch/back.php
	echo "You have been disconnected."
}

# Main
if [ "$1" == "--connect" ]
	then echo "Connection initialized"

	# check if inline password is provided or not
	if [ -z "$2" ] 
	then
		echo -n "Please provide the enclair password : "
		read -s password
		echo
	else 
		password=$2
	fi

	echo "... try to connect with the provided password"
	connect $password

elif [ "$1" == "--disconnect" ]
	then disconnect
fi

exit 0