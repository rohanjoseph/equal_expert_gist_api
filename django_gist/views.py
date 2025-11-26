from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
import requests
# Create your views here.1

GITHUB_API_URL = "https://api.github.com/users/{username}/gists"

headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def getData(request,username):
    response = requests.get(GITHUB_API_URL.format(username=username),headers=headers,allow_redirects=True)
    print(GITHUB_API_URL.format(username=username))
    if response.status_code == 200:
        gists_data = response.json()
        print(gists_data)
        return HttpResponse(render(request, 'index.html', {'gists': gists_data}))
    else:
        return HttpResponse("Failed to fetch gists", status=response.status_code)

def getIndex(request):
    return HttpResponse(render(request, 'landing.html'))