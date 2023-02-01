import pymongo
from pymongo import MongoClient
import scrap as sc

cluster = MongoClient
db = cluster["database1"]

"""
def yaz(girilen):
    genel = db[f"{girilen}"]
    data1 = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]
    x = genel.insert_many(data1)
"""
#aranacaklar = ["Vicky","Richard","Sandy"]
"""
def okuParametre(girilen,parametre):
    genel = db[f"{girilen}"]
    liste = list(genel.find({"marka":{ "$in": parametre }}))
    return liste
"""

def okuAdminParametre(girilen,marka):
    genel = db[f"{girilen}"]
    liste = list(genel.find( { "marka":{ "$in": marka }, "site": "bizimsite" } ))
    return liste

def okuParametre(girilen,marka,site):
    genel = db[f"{girilen}"]
    print(len(marka))
    print(len(site))
    if len(marka) ==0:
        liste = list(genel.find({"site":{ "$in": site }}).sort([("model", -1), ("fiyat", 1)]))
    else:
        liste = list(genel.find({"marka":{ "$in": marka }}).sort([("model", -1), ("fiyat", 1)]))
        print(liste)
    return liste

def oku1(girilen):
    genel = db[f"{girilen}"]
    liste = list(genel.find().sort([("model", -1), ("fiyat", 1)]))
    return liste

def okuAdmin():
    genel = db["genell"]
    liste = list(genel.find({"site": "bizimsite"}).sort([("model", -1), ("fiyat", 1)]))
    return liste

def databaseyaz():
    liste = sc.teknosa()
    liste1 = sc.vatan()
    liste.extend(liste1)
    genel = db["genel"]
    x = genel.insert_many(liste)

def updateData():
    #liste = sc.teknosa()
    #liste1 = sc.vatan()
    liste4 = sc.bizimsite()
    #liste2 = sc.incehesap()
    liste3 = sc.n11()
    #liste.extend(liste1)
    liste3.extend(liste4)
    #liste.extend(liste2)
    #liste.extend(liste4)
    
    for i in liste3:
        data = i
        querrry= {"site": i.get("site"),"model":i.get("model")}
        db["genell"].update_one(querrry,{ "$set": data },upsert = True)

def updateAdmin(eklenecek):
    data = eklenecek
    querrry= {"site": eklenecek.get("site"),"model":eklenecek.get("model")}
    db["genell"].update_one(querrry,{ "$set": data },upsert = True)

def silAdmin(eklenecek):
    liste = okuAdmin()
    data = liste[int(eklenecek)]
    querrry= {"site": liste[int(eklenecek)].get("site"),"model":liste[int(eklenecek)].get("model")}
    db["genell"].delete_one(querrry)

def okuParametreTek(site,model):
    querrry= {"site": f"{site}","model":f"{model}"}
    return db["genell"].find_one(querrry)

#updateData()
