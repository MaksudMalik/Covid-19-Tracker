import requests
import json
i=input("Enter country : ")
try:
    pg=requests.get("https://covid19.mathdro.id/api/countries/{}".format(i))
    js=json.loads(pg.text)
    con=js["confirmed"]["value"]
    rec=js["recovered"]["value"]
    det=js["deaths"]["value"]
    print ("\nConfirmed : {} \nRecovered : {}\nDeaths : {} ".format (con,rec,det))
    print("Last Update :",js["lastUpdate"][:10],",",js["lastUpdate"][11:-5],"000Z")
except:
	print("Enter a valid Country")