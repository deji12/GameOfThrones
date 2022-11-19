from rest_framework import serializers
from QuoteApp.models import Quote, Actor

'''
    Creating serializers for each 
    model 
'''

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'