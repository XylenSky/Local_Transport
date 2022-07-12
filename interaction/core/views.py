import os
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from secrets import token_hex

key = 1
min = 1

# Create your views here.


def get_html_content(city):
    import requests

    USER_AGENT = "Mozilla/5.0 (X11; " \
                 "Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(' ', '+')
    url = f"https://www.google.com/search?q=weather+in+{city}"
    print(url)
    html_content = session.get(url).text
    return html_content


def home(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        weather_data = dict()
        soup = BeautifulSoup(html_content, "html.parser")
        weather_data['region'] = soup.find('span', class_='BNeawe tAd8D AP7Wnd').text
        weather_data['daytime'] = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
        weather_data['temp'] = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
        # Fetch Weather data
    return render(request, "core/home.html", {'weather': weather_data})


def upload(request):
    global key
    url = []
    if request.method == 'POST':
        fs = FileSystemStorage()
        # print(request.POST.get('key'))
        if request.POST.get('key') == f'{key}':
            if request.FILES.get('document'):
                uploaded_file = request.FILES['document']
                if not(fs.exists(uploaded_file.name)):
                    fs.save(uploaded_file.name, uploaded_file)
            for files in os.listdir(settings.MEDIA_ROOT):
                url.append({'name': f'{files}', 'url': f'{fs.url(files)}'})
            key = token_hex(6)
            if min:
                print(key)
        else:
            url.append({'name': f'ask for key'})
    return render(request, 'core/upload.html', {'urls': url})
