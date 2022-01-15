#feh for images
#vlc/cvlc for videos

 #DISPLAY=:0 feh -x -F -Y rpiImager.png
 #no borders fullscreen no pointer

from urllib.request import urlopen
import requests
import time
  
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
def createDownloadedFilesList(fN, id):
    print('updating list of files')
    k=open('filesList.txt','a')
    k.write(fN+','+id+'\n')
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

    
while True:
    jsonVals=callAPI()
    # print(len(jsonVals))
    #print(jsonVals[0])
    dF=readDownloadedFiles()
    print(dF)
    for i in range(0,len(jsonVals)):
        if((jsonVals[i]['fileName']+','+jsonVals[i]['url']) in dF):
            doNothing=1
        else:
            createDownloadedFilesList(jsonVals[i]['fileName'],jsonVals[i]['url'])
            fileDownload('media/'+jsonVals[i]['fileName'],jsonVals[i]['url'])
      
        # if('default' in jsonVals[i]['fileName']):
        #     fileDownload('media/default',jsonVals[i]['url'])
            

    time.sleep(5)