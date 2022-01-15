#feh for images
#vlc/cvlc for videos

 #DISPLAY=:0 feh -x -F -Y rpiImager.png
 #no borders fullscreen no pointer

 #DISPLAY=:0 feh default.png & sleep 5 ; kill $!
 #display and kill after 5 seconds

from urllib.request import urlopen
import requests
import time
from os.path import exists
from filesHandler import *


  
# import json
import json
# store the URL in url as
# parameter for urlopen
jsonVals=None
def fileDownload(fileName, urlV):
    print('downloading file')
    urlValues=urlV.split('.')
    fileExtension=urlValues[len(urlValues)-1]
    url = urlV
    r = requests.get(url, allow_redirects=True)
    open(fileName, 'wb').write(r.content)
    print('file downloaded')

def callAPI():
    url = "https://mediascheduler-backend.production.rehanshakir.com/api/fields"
  
    # store the response of URL
    response = urlopen(url)
  
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
    return data_json
def createDownloadedFilesList(fN, id,tm,sec):
    print('updating list of files')
    k=open('filesList.txt','a')
    k.write(fN+','+id+','+tm+','+sec+'\n')
    k.close()
    print('updated list of files')
def readDownloadedFiles():
    try:
        g=open('filesList.txt','r')
        mm=g.read()
        g.close()
        kk=mm.split('\n')
        return kk
    except:
        print('e')
        return []


default_image_exists = exists('media/default.png')
if(default_image_exists):
    openDefaultImage()


while True:
    jsonVals=callAPI()
    dF=readDownloadedFiles()
    print(dF)
    for i in range(0,len(jsonVals)):
        if((jsonVals[i]['fileName']+','+jsonVals[i]['url']+','+jsonVals[i]['time']+','+jsonVals[i]['sec']) in dF):
            doNothing=1
        else:
            createDownloadedFilesList(jsonVals[i]['fileName'],jsonVals[i]['url'],jsonVals[i]['time'],jsonVals[i]['sec'])
            fileDownload('media/'+jsonVals[i]['fileName'],jsonVals[i]['url'])
            if('default' in jsonVals[i]['fileName']):
                openDefaultImage()
            

    time.sleep(5)