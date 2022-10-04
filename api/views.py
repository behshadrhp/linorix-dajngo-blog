from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import EssaySerializers
from blog.models import Essay, Comment


@api_view(['GET'])
def getRoutes(request):
    # this function is for get Routes in api

    routes = [
        {'GET':'/api/essay/'},
        {'GET':'/api/essay/id/'},
        {'GET':'/api/essay/id/vote/'},

        {'POST':'/api/token/'},
        {'POST':'/api/token/refresh/'},
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def essayVote(request, pk):
    # this function is for vote essay

    essay = Essay.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    comment, created = Comment.objects.get_or_create(
        owner=user,
        essay=essay,
    )

    comment.value = data['value']
    comment.save()
    essay.VoteCount

    serializers = EssaySerializers(essay, many=False)
    return Response(serializers.data)