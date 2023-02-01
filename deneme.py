import string
from unittest import result
import firebase_admin
from firebase_admin import credentials,firestore
from firebase_admin import auth

cred = credentials.Certificate("firebase-cred.json")
firebase_admin.initialize_app(cred)

def dbdeneme(col,doc):

    db = firestore.client()

    result = db.collection(f'{col}').document(f"{doc}").get()
    liste = result.to_dict()
    print(liste)
    return liste

def dbdeneme1(col):

    db = firestore.client()

    result = db.collection(f'{col}').get()
    #liste = result.to_dict()
    #print(result)
    return result


def dbkayıt():
    db = firestore.client()
    db.collection('trendyol').add({"Marka":"Asus","Fiyat":"15000","Ram":"16"})
    db.collection('trendyol').add({"Marka":"Hp","Fiyat":"17000","Ram":"16"})
    db.collection('trendyol').add({"Marka":"Apple","Fiyat":"25000","Ram":"8"})

def dbkayıt1():
    db = firestore.client()
    db.collection('testtt').document("Model1").set({"Marka":"Asus","Fiyat":"15000","Ram":"16","foto":"https://cdn.vatanbilgisayar.com/Upload/PRODUCT/acer/thumb/134837-1-2_small.jpg","link":"https://www.vatanbilgisayar.com/acer-aspire-3-3-nesil-ryzen-5-3500u-8gb-256gb-ssd-15-6inc-freedos.html"})
    db.collection('testtt').document("Model2").set({"Marka":"Hp","Fiyat":"17000","Ram":"16","foto":"https://cdn.vatanbilgisayar.com/Upload/PRODUCT/huawei/thumb/132694-1_small.jpg","link":"https://www.vatanbilgisayar.com/acer-aspire-3-3-nesil-ryzen-5-3500u-8gb-256gb-ssd-15-6inc-freedos.html"})
    db.collection('testtt').document("Model3").set({"Marka":"Apple","Fiyat":"25000","Ram":"8","foto":"https://cdn.vatanbilgisayar.com/Upload/PRODUCT/lenovo/thumb/132731-2-1_small.jpg","link":"https://www.vatanbilgisayar.com/acer-aspire-3-3-nesil-ryzen-5-3500u-8gb-256gb-ssd-15-6inc-freedos.html"})
