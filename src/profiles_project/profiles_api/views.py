from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API View"""
    def get(self, request, format=None):
        """ Return a list of ApiView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'It is similar to traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})