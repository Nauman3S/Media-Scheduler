#feh for images
#vlc/cvlc for videos

 #DISPLAY=:0 feh -x -F -Y rpiImager.png
 #no borders fullscreen no pointer

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
jsonVals=None
def callAPI():
    url = "https://mediascheduler-backend.production.rehanshakir.com/api/fields"
  
    # store the response of URL
    response = urlopen(url)
  
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
    return data_json

jsonVals=callAPI()
print(len(jsonVals))
print(jsonVals[0])
