#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
# Create your views here.
class HelloView(APIView):
    """TEst Api view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Return a list of APIView feature"""
        an_apiview =[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to the tradition django view',
            'Gives you most control over your application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request):
        """create Hello request with our name"""
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            
    def put(self,request,pk=None):
        """handle put request"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """handle partial update"""
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        """handle delete"""
        return Response({'method':'delete'})
        
class HelloViewSet(viewsets.ViewSet):
    """Api view set"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_viewset =[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Automatically map to URLs using Routers',
            'Provide more functionality with less code'
        ]
        return Response({"message":"hello",'a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})