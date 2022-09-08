#Web Scraping 2 websites and comparing the prize of a certain product to find the cheapest prize
import requests as r
from bs4 import BeautifulSoup as bs
           

def iphone12(gb):
    if gb==64:
        URLreliance64="https://www.reliancedigital.in/apple-iphone-12-64-gb-black/p/491901528"
        pagereliance64 = r.get(URLreliance64)
        soupreliance64 = bs(pagereliance64.content, "html.parser")
        pricereliance64=soupreliance64.find("span",{"class":"pdp__offerPrice"}).get_text()
        s_reliance64=""
        for i in pricereliance64:
            if i.isdigit() or i==".":
                s_reliance64+=i
        Pricereliance64=float(s_reliance64)        


        URLflipkart64="https://www.flipkart.com/apple-iphone-12-red-64-gb/p/itm3481e4053d500?pid=MOBFWBYZDP6QCQ8F&lid=LSTMOBFWBYZDP6QCQ8FB3JD1L&marketplace=FLIPKART&q=iphone+12&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=90b14721-e158-4cdb-bfe7-d7bae4f71f6d.MOBFWBYZDP6QCQ8F.SEARCH&ppt=hp&ppn=homepage&ssid=utaqrysjcw0000001648696296986&qH=7b7504afcaf2e1ea"
        pageflipkart64 = r.get(URLflipkart64)
        soupflipkart64 = bs(pageflipkart64.content, "html.parser")
        priceflipkart64=soupflipkart64.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
        s_flipkart64=""
        for i in priceflipkart64:
            if i.isdigit() or i==".":
                s_flipkart64+=i
        Priceflipkart64=float(s_flipkart64)        

        if Priceflipkart64<Pricereliance64:
            print("iphone(64gb) is less costly in Flipkart:-",Priceflipkart64)
            
        else:
            print("iphone(64gb) is less costly in Reliance:-",Pricereliance64)
            
            
    elif gb==128:
        URLreliance128="https://www.reliancedigital.in/apple-iphone-12-128-gb-blue/p/491901536"
        pagereliance128 = r.get(URLreliance128)
        soupreliance128 = bs(pagereliance128.content, "html.parser")
        pricereliance128=soupreliance128.find("span",{"class":"pdp__offerPrice"}).get_text()
        s_reliance128=""
        for i in pricereliance128:
            if i.isdigit() or i==".":
                s_reliance128+=i
        Pricereliance128=float(s_reliance128)        

        URLflipkart128="https://www.flipkart.com/apple-iphone-12-blue-128-gb/p/itm02853ae92e90a?pid=MOBFWBYZKPTZF9VG&lid=LSTMOBFWBYZKPTZF9VGE9ZTO4&marketplace=FLIPKART&q=iphone+12+128&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=621bd5c3-efc9-4318-b071-f27e24de3ebf.MOBFWBYZKPTZF9VG.SEARCH&ppt=hp&ppn=homepage&ssid=nk0fkgsaw00000001649310468184&qH=b8360ab59ca31390"
        pageflipkart128 = r.get(URLflipkart128)
        soupflipkart128 = bs(pageflipkart128.content, "html.parser")
        priceflipkart128=soupflipkart128.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
        s_flipkart128=""
        for i in priceflipkart128:
            if i.isdigit() or i==".":
                s_flipkart128+=i
        Priceflipkart128=float(s_flipkart128)        

        if Priceflipkart128<Pricereliance128:
            print("iphone(128gb) is less costly in Flipkart:-",Priceflipkart128)
            
        else:
            print("iphone(128gb) is less costly in Reliance:-",Pricereliance128)
            
        print("Sorry product not found")
item=input("enter the item")
if item=="iphone":
    product=input("enter the prodcut u want(if phone specify gb as well):-")
    if product in["iphone 64","IPHONE 64","Iphone 64","iphone64","IPHONE64","Iphone64","iphone 128","IPHONE 128","Iphone 128","iphone128","IPHONE128","Iphone128"]:
        s=""
        gb=0
        for i in product:
            if i.isdigit():
                s+=i
                gb=float(s)
        print(gb)
        iphone12(gb)        
