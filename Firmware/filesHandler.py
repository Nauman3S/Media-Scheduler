import ast
import subprocess,os
from subprocess import PIPE, run
import urllib.request  
import time

def openDefaultImage():
    os.system('(DISPLAY=:0 feh -x -F -Y media/default.png 2> /dev/null) &')