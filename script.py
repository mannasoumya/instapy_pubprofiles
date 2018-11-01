import requests
from bs4 import BeautifulSoup
import random
print("This script can only download photos from Public Instagram Profiles")
url=input("\nEnter Instagram Photo URL  (e.g. https://www.instagram.com/p/.../):- ")
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


outertag=soup.find_all('meta')
l=len(outertag)

for i in range(0,l):
    k=outertag[i].get('property')
    if(k=="og:image"):
        content=outertag[i].get('content')
        break

print("Your Photo is downloaded in the directory this script is running on...!!")
f = open((str(random.randint(1,50000)))+".jpg",'wb')
f.write(requests.get(content).content)
f.close()
