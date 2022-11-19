from django.shortcuts import render
from .models import Quote, Actor
import random
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def HomePage(request):

    all_actors = Actor.objects.all()

    if request.method == 'POST':
        name = request.POST.get("name")

        get_actor = Actor.objects.get(quoter=name)

        get_quotes = Quote.objects.filter(actor=get_actor)
        select_randomn_quote = random.choice(get_quotes)

        context = {
            "actors": all_actors,
            "quote": select_randomn_quote,
        }
        return render(request, 'home.html', context) 

    context = {
        "actors": all_actors
    }
    return render(request, 'home.html', context)