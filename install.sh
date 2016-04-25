#!/bin/bash
# curl -s https://raw.githubusercontent.com/epfl-dojo/framboise/master/install.sh | sudo bash -s --h

# Be sure to be root
if [ "$EUID" -ne 0 ]
	then echo "Please run me as root"
	exit
fi

# Default help message
help() {
	echo "Help:"
	echo " --cft	Install iceweasel (78.0 MB), vim (28.2 MB), ..."
	echo " --uar	update-upgrade-and-reboot"
}

# Be sure to get one arg
if [ "$#" -eq 0 ]
	then help
	exit
fi

update-upgrade-and-reboot () {
	apt-get update -y && apt-get upgrade -y && reboot
}

comfort () {
	apt-get install -y iceweasel vim
}

# http://superuser.com/questions/186272/check-if-any-of-the-parameters-to-a-bash-script-match-a-string
# idiomatic parameter and option handling in sh
while test $# -gt 0
do
	case "$1" in
		--all)
			echo "option 1"
			;;
		--install_only)
			echo "option 2"
			;;
		--cft)
			comfort
			;;
		--h)
			help
			;;
		--uar)
			update-upgrade-and-reboot
			;;
		--*)
			echo "bad option $1"
			help
			;;
		*)
			echo "invalid argument $1"
			help
			;;
	esac
	shift
done

exit 0