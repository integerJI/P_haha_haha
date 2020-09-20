from django.shortcuts import render
from .models import Blog
import requests
from bs4 import BeautifulSoup

githubId = input('아이디를 입력하세요 => ')
url = 'https://github.com/{}?tab=repositories'.format(githubId)
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

repositoriesList = soup.select('#user-repositories-list > ul')[0]
for repository in repositoriesList:
    repoName = repository.find('a')
    try:
        print(repoName.text, end='')
    except:
        pass

index = 0

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def test(request):
    return render(request, 'test.html')

def gogo(request):

    print('gogo 호출')
    
    for key in keyword:
        key = key.find('a')

        print(key.text)

    return render(request, 'test.html')

