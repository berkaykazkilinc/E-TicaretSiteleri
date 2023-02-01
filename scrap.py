from bs4 import BeautifulSoup
import requests
import pandas as pd

def vatan():
    liste = []
    tagler = ["Ram (Sistem Belleği)","Disk Türü","Disk Kapasitesi","İşlemci Numarası","Ekran Boyutu","İşletim Sistemi"]
    markalar = ["HUAWEI","ACER","ASUS","APPLE","CASPER","DELL","MSI","LENOVO","HP","HONOR","HOMETECH"]
    sayfa = 1
    while sayfa <=1:
        r = requests.get("https://www.vatanbilgisayar.com/notebook/?page="+str(sayfa))
        soup = BeautifulSoup(r.content,"lxml")
        
        st1=soup.find("div",attrs={"class":"wrapper-product wrapper-product--list-page clearfix"})
        st2=st1.find_all("div",attrs={"class":"product-list product-list--list-page"})
        sayfa= sayfa+1
        sayac = 0
        for ürün in st2:
            link ="https://www.vatanbilgisayar.com"+ ürün.a.get("href")
            model = ürün.find("div",attrs={"class":"product-list__product-code"}).text.strip('\n ')
            baslık = ürün.find("div",attrs={"class":"product-list__product-name"}).text.strip('\n ')
            fiyat = ürün.find("span",attrs={"class":"product-list__price"}).text.strip('\n ').replace(".","")
            #print(model)
            print(f"vatan: {fiyat}")
            print("------------------------------------------------------------------------------------------")
            r1 = requests.get(link)
            soup1 = BeautifulSoup(r1.content,"lxml")
            marka = soup1.find_all("a",attrs={"class":"bradcrumb-item"})
            markaa = ""
            #print(başlık)
            for a in marka:
                if a.text in markalar:
                    #print(a.text)
                    markaa= a.text
            st3 = soup1.find("div",attrs={"class":"clearfix"})
            foto = st3.a.get("href")
            st4 = soup1.find("div",attrs={"class":"col-lg-8 col-md-8 col-sm-8 col-xs-12"})
            puan = st4.find("strong").text
            st5 = soup1.find("div",attrs={"class":"row masonry-tab"})
            özellikler = st5.find_all("div",attrs={"class":"col-lg-6 col-md-6 col-sm-12 col-xs-12 property-tab-item"})
            #liste.append([link,model,foto,puan])
            liste1 = []
            for özellik in özellikler:
                table_rows = özellik.find_all("tr")
                for tr in table_rows:
                    td = tr.find_all('td')
                    #row = [i.text for i in td]
                    #print(row)
                    etiket= ""
                    deger = ""
                    for i in td:
                        if sayac == 1:
                            #print(i.text.strip("\n \xa0 İzle"))
                            #liste1.append(i.text.strip("\n \xa0 İzle"))
                            deger = i.text.strip("\n \xa0 İzle")
                            liste1.append({f"{etiket}": f"{deger}"})
                        if i.text in tagler:
                            sayac = 1
                            etiket = i.text
                        else:
                            sayac = 0
                    sayac=0
            markaa = markaa.upper()
            thisdict = {
                "site": "vatan",
                "model": model,
                "marka": markaa,
                "fiyat": fiyat,
                "puan" : puan,
                "özellikler" : liste1,
                "baslik" : baslık,
                "foto" : foto,
                "link" : link,
            }
            liste.append(thisdict)
            #liste.append([markaa,fiyat,model,puan,liste1,başlık,foto,link])
    return liste

#deneme = vatan()
#for i in deneme:
#    print(i)
#    print("-------------------------")

def teknosa():
    sayfa = 1
    liste = []
    tagler = ["SSD Kapasitesi","Disk Türü","Model Kodu","Ram","HDD Kapasitesi","Ekran Boyutu","İşlemci Modeli","İşletim Sistemi Yazılımı"]
    while sayfa <=1:
        r = requests.get("https://www.teknosa.com/arama?s=notebook%3Arelevance&page="+str(sayfa))
        soup = BeautifulSoup(r.content,"lxml")
        
        st1=soup.find("div",attrs={"class":"products"})
        st2=st1.find_all("div",attrs={"class":"prd"})

        sayfa= sayfa+1
        
        
        for ürün in st2:
            sayac = 0
            #link ="https://www.teknosa.com/asus-x415faek06626-intel-core-i310110u-14-8-gb-ram-1-tb-ssd-fhd-windows-10-home-laptop-p-786281775"
            link ="https://www.teknosa.com"+ ürün.a.get("href")
            title = ürün.find("a",attrs={"class":"prd-link"}).get("title")
            foto1 = ürün.find("div",attrs={"class":"prd-media"})
            foto = foto1.find("img",attrs={"class":"lazy"}).get("data-srcset")
            #print(foto)
            #print(title)
            r1 = requests.get(link)
            soup1 = BeautifulSoup(r1.content,"lxml")
            q1 = soup1.find("div",attrs={"class":"pdp-block2 pdpGeneralWidth"})
            marka = q1.find("b").text
            fiyat = q1.find("span",attrs={"class":"prc prc-last"}).text.strip(" TL")
            deneme = fiyat.split(",")
            for i in deneme:
                deneme = i.replace(".","")
                break
            fiyat = deneme
            print(f"teknosa: {fiyat}")
            print("------------------------------------------------------------------------------------------")
            puan = 0
            model = ""
            özellikler = soup1.find("div",attrs={"class":"ptf-body"})
            #liste.append([link,model,foto,puan])
            liste1 = []
            alınacaklar = []
            alınacaklarlistesi = []
            table_rows = özellikler.find_all("tr")
            al = 0
            for tr in table_rows:
                sayacilk = sayac
                th = tr.find_all('th')
                for i in th:
                    if i.text in tagler:
                        alınacaklar.append(sayac)
                        if i.text == "Model Kodu":
                            #print(i.text)
                            #print("1")
                            al = 1
                        #print(i.text)
                            
                    alınacaklarlistesi.append(i.text)
                    sayac+=1
                #print (sayac)
                if sayacilk == sayac:
                    sayac = sayac -4
                td = tr.find_all('td')
                for i in td:

                    #print(sayac)
                    #print(alınacaklar)
                    if sayac in alınacaklar:
                        #print(i.text)
                        if al == 1:
                            #print(i.text)
                            #print("2")
                            model = i.text
                            al = 0
                        else:
                            #print(alınacaklarlistesi)
                            #print(sayac)
                            print(alınacaklarlistesi[sayac])
                            #liste1.append(i.text)
                            liste1.append({f"{alınacaklarlistesi[sayac]}":f"{i.text}"})

                    #print(i.text)

                    sayac+=1
                #print("--------------------")
                if sayacilk > sayac:
                    sayac = sayac + 4

                #print (model)
                #print(alınacaklar)
            #print (model)
            marka = marka.upper()
            thisdict = {
                "site": "teknosa",
                "model": model,
                "marka": marka,
                "fiyat": fiyat,
                "puan" : puan,
                "özellikler" : liste1,
                "baslik" : title,
                "foto" : foto,
                "link" : link,
            }
            if model != "":
                liste.append(thisdict)
    return liste

def n11():
    r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar")
    soup = BeautifulSoup(r.content,"lxml")
    st1=soup.find("ul",attrs={"class":"list-ul"})
    st2=st1.find_all("li",attrs={"class":"column"})
    liste = []
    sayfa=1
    tagler = ["Marka","Disk Kapasitesi","Disk Türü","Model","Bellek Kapasitesi","HDD Kapasitesi","Ekran Boyutu","İşlemci Modeli","İşletim Sistemi"]

    while sayfa<=5:

        r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg="+str(sayfa))
        soup = BeautifulSoup(r.content,"lxml")

        st1=soup.find("ul",attrs={"class":"list-ul"})
        st2=st1.find_all("li",attrs={"class":"column"})
        
        
        for detaylar in st2:
            
            fiyat=detaylar.find("span",attrs={"class":"newPrice cPoint priceEventClick"}).text.replace("\n","").strip(" TL")
            deneme = fiyat.split(",")
            for i in deneme:
                deneme = i.replace(".","")
                break
            fiyat = deneme
            
            link=detaylar.a.get("href")
            r1 = requests.get(link)
            soup1 = BeautifulSoup(r1.content,"lxml")
           

            baslik=soup1.find("div",attrs={"class":"nameHolder"}).text.strip().replace("\n","")
            s=soup1.find("div",attrs={"class":"ratingCont"})
            puan=s.find("strong").text
            x=soup1.find("div",attrs={"class":"items"})
            urun_foto=x.img.get("data-lazy")
            marka=""
            model=""
            print(baslik,"\n",fiyat,"\n",puan,"\n",urun_foto)
            ozellikler=soup1.find("div",attrs={"class":"unf-prop-context"})
            detaylar=ozellikler.find_all("li",attrs={"class":"unf-prop-list-item"})
            liste1=[]
            for i in detaylar:
                etiket=i.find("p",attrs={"class":"unf-prop-list-title"}).text.strip(" ")
                deger=i.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip(" ")
                if(etiket in tagler):
                    if(etiket=="Marka"):
                        marka=deger
                    elif(etiket=="Model"):
                        model=deger
                    else:
                        liste1.append({f"{etiket}": f"{deger}"})
            marka = marka.upper()
            thisdict = {
                    "site": "n11",
                    "model": model,
                    "marka": marka,
                    "fiyat": fiyat,
                    "puan" : puan,
                    "özellikler" : liste1,
                    "baslik" : baslik,
                    "foto" : urun_foto,
                    "link" : link,
                }
            if (fiyat != "none" and model != ""):
                liste.append(thisdict)

        sayfa=sayfa+1

    return liste

def incehesap():
    liste = []
    sayfa=1
    tagler = ["Sistem Belleği","İşlemci Modeli","Model Kodu","SSD","İşletim Sistemi","İşletim Sistemi"]
    while sayfa<=5:

        r = requests.get("https://www.incehesap.com/notebook-fiyatlari/sayfa-"+str(sayfa))
        soup = BeautifulSoup(r.content,"lxml")

        st1=soup.find("div",attrs={"class":"grid grid-cols-2 md:grid-cols-3 gap-1"})
        st2=st1.find_all("a",attrs={"itemprop":"url"})

        for detaylar in st2:
            #print(i.get("href"))
            link_sonu=detaylar.get("href")
            link_basi="https://www.incehesap.com"
            link=link_basi+link_sonu
            r1=requests.get(link)
            soup1=BeautifulSoup(r1.content,"lxml")
            fiyat=soup1.find("div",attrs={"class":"price whitespace-nowrap text-2xl font-semibold !leading-none tracking-tight text-orange-500 md:text-4xl"}).text.strip(" TL")
            deneme = fiyat.split(",")
            for i in deneme:
                deneme = i.replace(".","")
                break
            fiyat = deneme.strip()
            st3=soup1.find("div",attrs={"class":"order-2 bg-white px-5 lg:order-3"})
            baslik=st3.find("h1").text.strip()
            try:
                marka=st3.find("a").text.strip()
            except:
                marka=("TOSHIBA")
            st4=soup1.find("div",attrs={"class":"relative my-auto"})
            puan = "0"
            resim_link_sonu=st4.find("img").get("data-src")
            resim_link=("https://www.incehesap.com")+resim_link_sonu
            st5=soup1.find("div",attrs={"class":"columns-1 md:columns-2 gap-5"})
            ozellikler=st5.find_all("tr")
            print(baslik,"\n",fiyat,"\n",marka,"\n",resim_link)
            liste1 = []
            model = ""
            for ozellik in ozellikler:
                etiket=ozellik.find("th").text.strip(" ")
                deger=ozellik.find("td").text.strip(" ")
                print(etiket,"=",deger)     
                if(etiket in tagler):
                        if(etiket=="Model Kodu"):
                            model=deger
                        else:
                            liste1.append({f"{etiket}": f"{deger}"})
            marka = marka.upper()
            thisdict = {
                        "site": "incehesap",
                        "model": model,
                        "marka": marka,
                        "fiyat": fiyat,
                        "puan" : puan,
                        "özellikler" : liste1,
                        "baslik" : baslik,
                        "foto" : resim_link,
                        "link" : link,
                    }
            if model != "":
                liste.append(thisdict)

        sayfa=sayfa+1
    return liste

def bizimsite():
    r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar")
    soup = BeautifulSoup(r.content,"lxml")
    st1=soup.find("ul",attrs={"class":"list-ul"})
    st2=st1.find_all("li",attrs={"class":"column"})
    liste = []
    sayfa=1
    tagler = ["Marka","Disk Kapasitesi","Disk Türü","Model","Bellek Kapasitesi","HDD Kapasitesi","Ekran Boyutu","İşlemci Modeli","İşletim Sistemi"]

    while sayfa<=5:

        r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg="+str(sayfa))
        soup = BeautifulSoup(r.content,"lxml")

        st1=soup.find("ul",attrs={"class":"list-ul"})
        st2=st1.find_all("li",attrs={"class":"column"})
        
        
        for detaylar in st2:
            
            fiyat=detaylar.find("span",attrs={"class":"newPrice cPoint priceEventClick"}).text.replace("\n","").strip(" TL")
            deneme = fiyat.split(",")
            for i in deneme:
                deneme = i.replace(".","")
                break
            fiyat = deneme
            
            link=detaylar.a.get("href")
            r1 = requests.get(link)
            soup1 = BeautifulSoup(r1.content,"lxml")
           

            baslik=soup1.find("div",attrs={"class":"nameHolder"}).text.strip().replace("\n","")
            s=soup1.find("div",attrs={"class":"ratingCont"})
            puan=s.find("strong").text
            x=soup1.find("div",attrs={"class":"items"})
            urun_foto=x.img.get("data-lazy")
            marka=""
            model=""
            print(baslik,"\n",fiyat,"\n",puan,"\n",urun_foto)
            ozellikler=soup1.find("div",attrs={"class":"unf-prop-context"})
            detaylar=ozellikler.find_all("li",attrs={"class":"unf-prop-list-item"})
            liste1=[]
            for i in detaylar:
                etiket=i.find("p",attrs={"class":"unf-prop-list-title"}).text.strip(" ")
                deger=i.find("p",attrs={"class":"unf-prop-list-prop"}).text.strip(" ")
                if(etiket in tagler):
                    if(etiket=="Marka"):
                        marka=deger
                    elif(etiket=="Model"):
                        model=deger
                    else:
                        liste1.append({f"{etiket}": f"{deger}"})
            marka = marka.upper()
            thisdict = {
                    "site": "bizimsite",
                    "model": model,
                    "marka": marka,
                    "fiyat": fiyat,
                    "puan" : puan,
                    "özellikler" : liste1,
                    "baslik" : baslik,
                    "foto" : urun_foto,
                    "link" : link,
                }
            if (fiyat != "none" and model != ""):
                liste.append(thisdict)

        sayfa=sayfa+1

    return liste