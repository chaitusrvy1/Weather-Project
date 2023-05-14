from django.shortcuts import render
from django.http import HttpResponse

import requests

from bs4 import BeautifulSoup
from datetime import datetime

# Create your views here.

url='https://www.msn.com/en-in/weather/forecast/in-Balanagar,TG?loc=eyJsIjoiQmFsYW5hZ2FyIiwiciI6IlRHIiwicjIiOiJNZWRjaGFsIiwiYyI6IkluZGlhIiwiaSI6IklOIiwiZyI6ImVuLWluIiwieCI6Ijc4LjQ3MDAwMTIyMDcwMzEyIiwieSI6IjE3LjQ1MDAwMDc2MjkzOTQ1MyJ9&weadegreetype=C'

res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')


def index(request):
    return render(request,'index.html')


def home(request,soup=soup):
    data=soup.find('a',class_='location_name_main_container-E1_1')
    data1=soup.find('a',class_='summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1')
    data2=soup.find('div',class_='cap-E1_1')
    data3=soup.find('p',class_='summaryDescCompact-E1_1')
    date=datetime.today().date
    print(data3)

    return render(request,'home.html',{'city':data.text,'temperature':data1.text,'description':data2.text,'date':date,'content':data3.text})



