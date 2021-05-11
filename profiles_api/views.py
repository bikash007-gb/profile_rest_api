#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloView(APIView):
    """TEst Api view"""
    def get(self,request,format=None):
        """Return a list of APIView feature"""
        an_apiview =[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to the tradition django view',
            'Gives you most control over your application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})