import ast
import subprocess,os
from subprocess import PIPE, run
import urllib.request  
import time

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout
def isVideoRunning():
    batcmd="ps -a | grep vlc"
    
    my_output1 = out(batcmd)
    print(my_output1)
    if("vlc" in my_output1):
        print('video is running')
        return True
    else:
        print('video is NOT running')
        return False
    
def openDefaultImage():
    os.system('(DISPLAY=:0 feh -x -F -Y media/default.png 2> /dev/null) &')

def openImage(fileName,sleepTime):
    os.system('(DISPLAY=:0 feh -x -F -Y media/' +fileName+' & sleep '+sleepTime+' ; kill $!)')

def playVideo(fileName):
    if(isVideoRunning()==False):
        os.system('(DISPLAY=:0 cvlc -I dummy --fullscreen --no-video-deco --no-embedded-video --no-osd --no-video-title --width=1920 --height=1080 --video-x=0 --video-y=-10 --play-and-exit --no-video-on-top media/' + fileName+ '  2> /dev/null) &')
    
def openTerminal():
    os.system('lxterminal')