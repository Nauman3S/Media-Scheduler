#-e option instructs bash to immediately exit if any command [1] has a non-zero exit status
# We do not want users to end up with a partially working install, so we exit the script
# instead of continuing the installation with something broken
set -e

echo "Media Scheduler Installer"
echo "*****RUN THIS SCRIPT AS A ROOT USER*****"
echo "This script will:"
echo "Clone and Install the Media Scheduler"
echo "Put the Media Scheduler in the startup sequence of the raspberry pi"

######## VARIABLES #########

# Location for final installation log storage
#installLogLoc=/etc/pihole/install.log


echo "Welcome user"
echo $USER
cd $HOME

show_ascii_berry() {
    echo -e "

Media Scheduler Installer

    "
}
show_ascii_berry

if [ -d "$HOME/Media-Scheduler" ]
then
    echo "Directory Media-Scheduler exists."
else
    echo "Error: Directory RPiClient does not exists."
    cd $HOME
    # mkdir ~/RPiClient
    git clone \
    https://github.com/Nauman3S/Media-Scheduler;
    cd Media-Scheduler
    
    
fi
if [ -d "$HOME/Media-Scheduler/logs" ]
then
    echo "Directory Media-Scheduler/logs exists."
else
    echo "Error: Directory RPiClient does not exists."
    mkdir $HOME/Media-Scheduler/logs
fi

File="/etc/rc.local"

if [[ $(grep "(sleep 8; sh /home/pi/Media-Scheduler/starter.sh)&" $File) ]] ; then
    echo "Found startup script. Doing nothing."
else
    echo "Not Found. Adding startup script"
    sed -i -e '$i \(sleep 8; sh /home/pi/Media-Scheduler/starter.sh)&\n' /etc/rc.local
fi



echo "Installtion Completed. Restart your Raspberry Pi"