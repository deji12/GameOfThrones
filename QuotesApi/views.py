from django.shortcuts import render
from rest_framework.decorators import api_view
from QuoteApp.models import Actor, Quote
from .serializers import ActorSerializer, QuoteSerializer
from rest_framework.response import Response
import random

@api_view(["GET"])
def Home(request):
    
    '''
        This view returns basic documentation for how to use the api
    '''
    
    return Response({
        "To generate randon quote by random actor": "https://gameofthrones-production.up.railway.app/api/",
        "TO get actors present": "https://gameofthrones-production.up.railway.app/api/get-all-actors/",
        "To generate quote from a specific actor": {
            "visit the url": "https://gameofthrones-production.up.railway.app/api/get-quot-by-actor/",
            "send post request with actor name as post data to the url": "post data variable must be named 'actor'"
        },
    })

@api_view(["GET"])
def get_all_actors_present(request):

    '''
        This view retrives all actors in the 
        database and returns the queryset to the client
    '''

    all_actors = Actor.objects.all()
    serializer = ActorSerializer(all_actors, many=True)
    return Response(serializer.data)

@api_view(["POST", "GET"])
def get_quote_by_actor(request):

    '''
        This view retrives and returns a random quote by
        an actor specified in the post request
        from the client
    '''

    if request.method == 'POST':
        actor = request.data.get("actor")

        get_actor = Actor.objects.get(quoter=actor)

        get_quotes = Quote.objects.filter(actor=get_actor)

        select_randomn_quote = random.choice(get_quotes)

        serializer = QuoteSerializer(select_randomn_quote, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def get_random_quote(request):

    '''
        This view returns a random quote from a random actor 
    '''

    all_quotes = Quote.objects.all()
    random_quote = random.choice(all_quotes)
    serializer = QuoteSerializer(random_quote, many=False)
    return Response(serializer.data)