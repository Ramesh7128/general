from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
            if 'register' in request.POST:
                email = request.POST.get('email')
                username = request.POST.get('username')
                payload = {'email': email, 'username': username}
                response = requests.get("https://thawing-crag-5040.herokuapp.com/general/register/", params=payload)
                content =  response.content
                context['cont'] = content
            elif 'submit' in request.POST:
                user_email = request.POST.get('user_email')
                answer = request.POST.get('answer')
                r = requests.get('https://thawing-crag-5040.herokuapp.com/general/sample_view/')
                csrf_token_value = r.cookies['csrftoken']
                cookies = dict(csrftoken=csrf_token_value)
                print csrf_token_value
                post_data = {'email': user_email, 'answer': answer}
                headers = {'Referer': "https://thawing-crag-5040.herokuapp.com/general/sample_view/", "Host": "thawing-crag-5040.herokuapp.com"}
                response = requests.post("https://thawing-crag-5040.herokuapp.com/general/sign_nda/", data=post_data, headers=headers, cookies=cookies)
                print response.content
    return render(request, 'challengeApp/index.html', context)