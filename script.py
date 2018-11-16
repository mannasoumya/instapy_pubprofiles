import requests
from bs4 import BeautifulSoup
import random

def download(url,option):    
    if(option==1):
        f = open((str(random.randint(1,50000)))+".jpg",'wb')
    elif(option==2):
        f = open((str(random.randint(1,50000)))+".mp4",'wb')
    f.write(requests.get(url).content)
    f.close()
    print("Your Media is downloaded in the directory this script is running on..")
    
print()
print("This script can only download photos and videos from \"Public Instagram Profiles\"")
url=input("\nEnter Instagram Post URL  :- ")
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
outertag=soup.find_all('meta')
l=len(outertag)
prop=[]
for i in range(0,l):
    prop.append(outertag[i].get('property'))

vc = False
for t in prop:
    if (t == "og:video"):
        vc=True

for i in range(0,l):
    k=outertag[i].get('property')
    if (vc==True and k == "og:video"):
        content=outertag[i].get('content')
        download(content,2)
        break
    if (vc==False and k == "og:image"):
        content=outertag[i].get('content')
        download(content,1)
        break
