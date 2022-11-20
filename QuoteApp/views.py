from django.shortcuts import render, redirect
from .models import Quote, Actor, IpLocation
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

@csrf_exempt
def HomePage(request):

    ip_address = get_location()
    new_ip_location = IpLocation(ip=ip_address['ip'], city=ip_address['city'], region=ip_address['region'], country=ip_address['country'])
    new_ip_location.save()


    '''
        This view accepts input
        from a post request from a form in the frontend 
        and querries the database and returns 
        a response containing a quote by whatever actor
        was specified in the post request
    '''

    all_actors = Actor.objects.all()

    if request.method == 'POST': # if user searches for quote by actor
        name = request.POST.get("name") # get actor selected in frontend

        if not name:
            messages.error(request, "Select an actor!") # checking if user selected any actor
            return redirect('home')

        get_actor = Actor.objects.get(quoter=name) # query for actor object

        get_quotes = Quote.objects.filter(actor=get_actor) # query for quotes by actor
        select_randomn_quote = random.choice(get_quotes) # select random quote from queryset

        context = { # return randomly selected quote
            "actors": all_actors,
            "quote": select_randomn_quote,
        }
        return render(request, 'home.html', context) 

    context = {
        "actors": all_actors
    }
    return render(request, 'home.html', context)