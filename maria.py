from os import pathsep
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
job_title=[]
jobs_type=[]
locations=[]
path=[]
result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src=result.content

soup=BeautifulSoup(src,"lxml")
comp=soup.find("div",{"id":"app"})
jobs=comp.find_all("div",{"class":"css-qa8nz1-Card e1v1l3u10"})
for job in jobs:
    title=job.find("a",{"class":"css-nn640c"}).text.strip()
    job_type=job.find("div",{"class":"css-1w0948b"}).text.strip()
    location=job.find("span",{"class":"css-5wys0k"}).text.strip()
    urls=job.find("a",{"class":"css-nn640c"})["href"]

    job_title.append(title)
    jobs_type.append(job_type)
    locations.append(location)
    path.append(urls)

file_list=[job_title,jobs_type,locations,path]
exported=zip_longest(*file_list)

with open("/Users/control/Desktop/webscrap/jobs.csv","w") as myfile:

    wr=csv.writer(myfile)    
    wr.writerow(["job title","job type","location","path"])
    wr.writerows(exported)