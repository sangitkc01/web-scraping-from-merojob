from bs4 import BeautifulSoup
import requests


final_data=[]
job=input("enter job = ")
n=int(input('enter pages = '))
for i in range(1,n+1):
    url=BeautifulSoup(f"https://merojob.com/search/?q={job}&start_date=&end_date=&page={i}","html.parser")
    res=requests.get(url)
    text=res.content
    soup=BeautifulSoup(text,"lxml")

    items=soup.find_all('div',class_="col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left")

    for item in items:
        job_name=item.find("h1",class_="text-primary font-weight-bold media-heading h4").a.text.strip()
        company_name=item.find("h3",class_="h6").a.text.strip()
        address=item.find("span",class_="text-muted").span.text.strip()
        skills=item.find_all("span",itemprop="skills")
        
        for skill in skills:
            skl=skill.text.strip().replace("\n"," , ")
            data={
                "Job Name ": job_name,
                "Company Name ": company_name,
                "Address ":address,
                "Skills ":skl
            }
        
     


        final_data.append(data)

import pandas as pd

df=pd.DataFrame(final_data)
dff=df.to_csv("merojob3.csv")
print(df)


