from flask import Flask,redirect,url_for,render_template,request
from flask_paginate import Pagination,get_page_args
import dbmongo as d1
import json

basılacak = [{"ad":"kaan","soyad":"güler"},{"ad":"hashüs"},{"ad":"kubi"},{"ad":"bilbo"}]

app = Flask(__name__)


@app.route('/akakceklon', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        #d1.dbkayıt1()
        markalar = request.form.getlist('mycheckbox')  
        siteler = request.form.getlist('mysite')
        examp = d1.okuParametre("genell",markalar,siteler)
        return render_template('alo.html', basılacak = examp)
    else:
        examp = d1.oku1("genell")
        return render_template('alo.html', basılacak = examp)

@app.route("/ak")
def akakce():
    return render_template('akakce.html')

@app.route("/trendyol/about")
def trendyol_about():
    return render_template('trendyol_about.html')

"""
def get_users(deneme,offset=0,per_page=20):
    return deneme[offset:offset+per_page]

"""

@app.route("/trendyol", methods=["GET", "POST"])
def trendyol_homepage(name="genell"):
    if request.method == "POST" : 
        markalar = request.form.getlist('mycheckbox')  
        examp = d1.okuAdminParametre("genell",markalar)
        print(examp)
        print("a")
        return render_template('trendyol_anasayfa.html', basılacak = examp)
    else:

        examp = d1.okuAdmin()

        return render_template('trendyol_anasayfa.html', basılacak = examp)

"""
@app.route("/trendyol", methods=["GET", "POST"])
def trendyol_homepage(name="genell"):
    if request.method == "POST" : 
        markalar = request.form.getlist('mycheckbox')  
        examp = d1.okuParametre("genell",markalar)
        print(examp)
        return render_template('trendyol_filtre.html', basılacak = examp)
    else:

        examp = d1.oku1(name)
        page,per_page,offset = get_page_args(page_parameter="page",per_page_parameter="per_page")

        total=len(examp)
        pagination_users = get_users(examp,offset=offset,per_page=per_page)

        pagination = Pagination(page=page,per_page=per_page,total=total,css_framework='bootstrap4')

        return render_template('trendyol_anasayfa.html', basılacak = pagination_users,page=page,per_page=per_page,pagination=pagination)
"""

@app.route("/trendyol/ic")
@app.route("/trendyol/ic/<name>/<name1>")
def trendyol_icsayfa(name,name1):
    examp = d1.okuParametreTek(name,name1)
    return render_template('trendyol_icsayfa.html',basılacak = examp)

@app.route('/kaan')
@app.route('/kaan/<name>/<name1>/<name2>')
def kaan(name,name1,name2):
    examp = d1.oku1("genell")
    examp1 = d1.okuParametreTek(name1,name2)
    return render_template('akakce.html', basılacak = examp, tekbas = examp1, name = name)

@app.route("/admin")
def admin(name="genell"):
    if request.method == "POST" : 
        markalar = request.form.getlist('mycheckbox')
        examp = d1.okuAdmin()
        return render_template('admin_page.html', basılacak = examp)
    else:

        examp = d1.okuAdmin()
        return render_template('admin_page.html', basılacak = examp)

@app.route("/form_duzenle/<name>", methods=["GET", "POST"])
def duzenle_form(name):

    if request.method == "POST":
        guncellenecek = request.form.getlist('textbar')
        print(request.form.getlist('textbar'))
        thisdict = {
                "site": "bizimsite",
                "model": guncellenecek[2],
                "marka": guncellenecek[1],
                "fiyat": guncellenecek[3],
                "puan" : guncellenecek[4],
                "özellikler" : eval(guncellenecek[6]),
                "baslik" : guncellenecek[0],
                "foto" : guncellenecek[5]
            }
        d1.updateAdmin(thisdict)
        return render_template('duzenlendi.html')
    else:
        examp = d1.okuAdmin()
        return render_template('duzenleme_form_page.html',basılacak = examp,i=name)

@app.route("/sil/<name>")
def sil(name):
        d1.silAdmin(name)
        #database silme fonksiyonu eklenicek
        return render_template('sil.html')

@app.route("/form_ekle" ,methods=["GET", "POST"])
def ekle_form():
    if request.method == "POST":
        guncellenecek = request.form.getlist('textbar')
        print(request.form.getlist('textbar'))
        thisdict = {
                "site": "bizimsite",
                "model": guncellenecek[2],
                "marka": guncellenecek[1],
                "fiyat": guncellenecek[3],
                "puan" : guncellenecek[4],
                "özellikler" : eval(guncellenecek[6]),
                "baslik" : guncellenecek[0],
                "foto" : guncellenecek[5]
            }
        d1.updateAdmin(thisdict)
        return render_template('eklendi.html')
    else:
        return render_template('ekleme_form_page.html')

if __name__ == "__main__":
    app.run(debug= True)
    #app.run(host="0.0.0.0", port=5000, debug=True)