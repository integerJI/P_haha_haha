from django.shortcuts import render
from .models import Blog
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.daum.net/').text
soup = BeautifulSoup(source, 'html.parser')
keyword= soup.select('span.txt_ranking')

index = 0

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def test(request):
    return render(request, 'test.html')

def gogo(request):

    print('gogo 호출')
    
    for key in keyword:
        print(key.text)

    return render(request, 'test.html')

