from requests import post,get

requrl = "http://localhost:8000/GIS/request/"
logurl = "http://localhost:8000/GIS/login/"
#print(post(requrl,data = {'RequestID':'1','IncidentType':'Fire','image':'','Latitude':'28.627137','Longitude':'77.435281','Details':'fire Emergency !!'}).text)
#print(post(requrl,data = {'RequestID':'2','IncidentType':'Earthquake','image':'','Latitude':'45.627137','Longitude':'87.435281','Details':'Earthquake Emergency!!'}).text)
#print(post(logurl,data = {'username':'ghaziabad','password':'ghaziabad123'}).text)

def getRequest(rid):
    print(get(requrl+'?rid='+rid).text)

if __name__ == "__main__":
    getRequest('1')
