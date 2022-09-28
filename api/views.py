from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from .serializers import EssaySerializers
from blog.models import Essay

from api import serializers


@api_view(['GET'])
def getRoutes(request):
    # this function is for get Routes in api

    routes = [
        {'GET':'/api/essay'},
        {'GET':'/api/essay/id'},
        {'GET':'/api/essay/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
def getEssays(request):
    # this function is for serializers for essays

    essay = Essay.objects.all()
    serializers = EssaySerializers(essay, many=True)

    return Response(serializers.data)

@api_view(['GET'])
def getEssay(request, pk):
    # this function is for serializers for essay

    essay = Essay.objects.get(id=pk)
    serializers = EssaySerializers(essay, many=False)

    return Response(serializers.data)