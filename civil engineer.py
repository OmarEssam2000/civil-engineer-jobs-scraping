#1st step install and import modules
import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest
job_titles = []
locations = []

#2nd step use requests to fetch the url
URL = "https://wuzzuf.net/search/jobs/?a=hpb&q=civil%20engineer&start="

#3rd step save page content/markup
for page in range(1,10):
      # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example
  
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')
  
    job_title = soup.find_all('h2',attrs={'class':'css-m604qf'})
    location = soup.find_all('span',attrs={'class':'css-5wys0k'})
  
    for title in job_title:
        job_titles.append(title.text)
    for locate in location:
        locations.append(locate.text) 

        
#4th step create soup object to parse content

#5th step find the elements containing info we need
#-- job titles, job skills, company names, location names الحاجات اللى احنا عايزينها

#6th step loop over returned lists to extract needed info into other lists

    

#7th step create csv file and fill it with values
file_list = [job_titles , locations]
exported = zip_longest(*file_list) #دي الفانكشن اللى بتجيب واحد من كل ليسته جنب بعض 
with open("E:/programming/web scraping/civil engineer jobs.csv" , "w" ) as myfile :
    wr = csv.writer(myfile)
    wr.writerow(["job titles" , "locations"])
    wr.writerows(exported)