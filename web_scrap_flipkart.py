import requests
from bs4 import BeautifulSoup
import csv
topic=['Name','Price','Rating']
name=[]
price=[]
rating=[]
def reques():
    req=response.text
    soup=BeautifulSoup(req,'html.parser')
    formatted_req=soup.prettify()
    for i in soup.find_all("div",class_="_3wU53n"):
        name.append(i.get_text())
    for i in soup.find_all('div',class_='_1vC4OE _2rQ-NK'):
        price.append(i.get_text())
    for i in soup.find_all('div',class_="hGSR34"):
        rating.append(i.get_text())
url1="https://www.flipkart.com/laptops/hp~brand/pr?sid=6bo,b5g&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_laptops-store_ZCQFAP2R5I_wp3&fm=neo%2Fmerchandising&iid=M_788221d6-9dfe-4d06-87c3-5ad4a9f04a2a_5.ZCQFAP2R5I&ppt=clp&ppn=laptops-store&ssid=vl57zyqa800000001590942010486"
response=requests.get(url1)
reques()
url2='https://www.flipkart.com/laptops/hp~brand/pr?sid=6bo%2Cb5g&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_laptops-store_ZCQFAP2R5I_wp3&fm=neo%2Fmerchandising&iid=M_788221d6-9dfe-4d06-87c3-5ad4a9f04a2a_5.ZCQFAP2R5I&ppt=clp&ppn=laptops-store&ssid=vl57zyqa800000001590942010486&page=2'
response=requests.get(url2)
reques()
url3='https://www.flipkart.com/laptops/hp~brand/pr?sid=6bo%2Cb5g&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_laptops-store_ZCQFAP2R5I_wp3&fm=neo%2Fmerchandising&iid=M_788221d6-9dfe-4d06-87c3-5ad4a9f04a2a_5.ZCQFAP2R5I&ppt=clp&ppn=laptops-store&ssid=vl57zyqa800000001590942010486&page=3'
response=requests.get(url3)
reques()
url4='https://www.flipkart.com/laptops/hp~brand/pr?sid=6bo%2Cb5g&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_laptops-store_ZCQFAP2R5I_wp3&fm=neo%2Fmerchandising&iid=M_788221d6-9dfe-4d06-87c3-5ad4a9f04a2a_5.ZCQFAP2R5I&ppt=clp&ppn=laptops-store&ssid=vl57zyqa800000001590942010486&page=4'
response=requests.get(url3)
reques()
url5='https://www.flipkart.com/laptops/hp~brand/pr?sid=6bo%2Cb5g&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_laptops-store_ZCQFAP2R5I_wp3&fm=neo%2Fmerchandising&iid=M_788221d6-9dfe-4d06-87c3-5ad4a9f04a2a_5.ZCQFAP2R5I&ppt=clp&ppn=laptops-store&ssid=vl57zyqa800000001590942010486&page=5'
response=requests.get(url3)
reques()
temp=[]
with open ('list.csv','w', encoding='UTF-8',newline='') as f:
    csv_writer=csv.writer(f)
    x=zip(name,price,rating)
    csv_writer.writerows(x)

with open ('list.csv','r',encoding='UTF-8') as f:
    csv_reader=list(csv.reader(f))
    for i in csv_reader:
        rem=i[1].replace('₹','').replace(',','')
        temp.append(rem)

with open ('list.csv','w', encoding='UTF-8',newline='') as f:
    csv_writer=csv.writer(f)
    x=zip(name,temp,rating)
    csv_writer.writerows(x)
with open ('list.csv','r',encoding='UTF-8') as f:
    csv_reader=list(csv.reader(f))
    # print(csv_reader)
    sorted_price=sorted(csv_reader,key=lambda x:int(x[1]),reverse=True)    
with open('sorted_price.csv','w',encoding='UTF-8',newline='') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(topic)
    for i in sorted_price:
        i[1]='₹'+str(i[1])
    csv_writer.writerows(sorted_price)
