
import requests as req
import re
class GoogleDirect():
    def __init__(self):
        self.apikey="AIzaSyDKK7r7KwkF-hE6OxSBRhOFk7vwzjDusMs"

    def getdirect(self,paramStarts,paramEnd):
        ret_dic=req.post("https://maps.googleapis.com/maps/api/directions/json?origin="+paramStarts+"&destination="+paramEnd+"&key="+self.apikey).json()
        htmlre=re.compile('>(.*?)<')
        temp_steps=ret_dic["routes"][0]["legs"][0]["steps"]
        ret=""
        for tem in temp_steps:
            ret=ret+"---"+''.join(htmlre.findall(tem["html_instructions"]))
        return ret
